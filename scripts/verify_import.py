"""Import every generated module, and byte-compile the ones that can't be imported.

Run against the installed wheel, not the working tree, so this checks what we would
actually publish.

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

print(f"verify: imported {count} modules")
