"""Import every generated module, and byte-compile the ones that can't be imported.

Run against the installed wheel, not the working tree, so this checks what we would
actually publish. Given a path, it also checks the recorded API surface (see
api_surface.py), reusing the imports this walk has already done.

`import incident_io` only pulls in the client and, transitively, the model graph — about
four fifths of the package. Every module under `incident_io.api` is left out, because
`api/__init__.py` imports nothing and each operation lives in its own module. Those are
the modules callers actually reach for, and a wheel ships source rather than bytecode, so
a name error in one of them would go out undetected.
"""

import compileall
import importlib
import pkgutil
import sys
from pathlib import Path

import incident_io

package_root = incident_io.__path__[0]

# Catches syntax errors anywhere in the tree, including any module that import alone would
# never reach. quiet=1 prints errors but not filenames.
if not compileall.compile_dir(package_root, quiet=1, force=True):
    sys.exit("verify: byte-compilation failed")


def _raise(name: str) -> None:
    """walk_packages swallows import errors while discovering subpackages unless it is
    given an onerror. Swallowing them is exactly the failure this script exists to catch."""
    raise ImportError(f"failed to import {name}")


count = 0
for module in pkgutil.walk_packages(incident_io.__path__, "incident_io.", onerror=_raise):
    importlib.import_module(module.name)
    count += 1

# A floor, because the count on its own proves nothing: a schema that generated
# five modules, or a generator that silently dropped every endpoint, imports
# perfectly. The real figure is ~1900; this only catches collapse.
MINIMUM_MODULES = 1000
if count < MINIMUM_MODULES:
    sys.exit(
        f"verify: only {count} modules, expected at least {MINIMUM_MODULES}. "
        f"The generator produced far less than it should have."
    )

# Checked here rather than only in the tests, because the release path runs
# this and `make generate` recreates the marker on every run.
if not (Path(package_root) / "py.typed").exists():
    sys.exit("verify: py.typed is missing, so type checkers will ignore the SDK")

print(f"verify: imported {count} modules")

# Folded in here rather than run as its own command: every module is already
# in sys.modules, so recording the surface costs nothing, where a second
# process would import the whole package again.
if len(sys.argv) > 1:
    sys.path.insert(0, str(Path(__file__).parent))
    from api_surface import check, surface

    raise SystemExit(check(surface("incident_io"), Path(sys.argv[1])))
