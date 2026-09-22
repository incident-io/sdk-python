# Pinned deliberately: this generator changes its own output in minor releases,
# which would reshape our public API. Upgrade by hand and read the diff.
OPC_VERSION := 0.29.1

# The generator declares ruff>=0.2 with no upper bound and runs it as a post
# hook, so an unpinned resolve reformats all 1895 files the day ruff changes
# its formatter: drift goes red on every unrelated PR, and the next release
# commits a whole-tree reformat labelled as a schema change.
RUFF_VERSION := 0.16.8

PACKAGE    := incident_io
SCHEMA_URL := https://api.incident.io/v1/openapiV3.json

.PHONY: fetch generate verify surface clean

# -L because without it a redirect is a silent success writing zero bytes,
# which parses as an empty schema.
fetch:
	curl -sfSL $(SCHEMA_URL) -o openapi.json

# --meta none keeps the generator to the package itself. Any other value has it
# write pyproject.toml and README.md too, overwriting ours.
generate: openapi.json
	rm -rf $(PACKAGE)
	uvx --from openapi-python-client==$(OPC_VERSION) --with ruff==$(RUFF_VERSION) \
		openapi-python-client generate \
		--path openapi.json \
		--output-path $(PACKAGE) \
		--meta none \
		--config config.yml \
		--overwrite \
		--fail-on-warning
	python3 scripts/fix_generated.py $(PACKAGE)
	python3 scripts/mark_deprecated.py openapi.json $(PACKAGE)
	# Committed too, but recreated here because generate removes the package
	# first. Without it type checkers ignore every annotation in the SDK.
	touch $(PACKAGE)/py.typed

# Pinned: verify gates the release, so a new check in a mypy release would
# halt the hourly pipeline rather than fail a pull request.
MYPY_VERSION := 2.3.1

# Python has no compile step, so we install the wheel and exercise it. See
# scripts/verify_import.py for why importing the package alone isn't enough.
verify:
	rm -rf dist
	uv build
	uv venv --clear .venv-verify
	uv pip install --quiet --python .venv-verify dist/*.whl mypy==$(MYPY_VERSION)
	.venv-verify/bin/python scripts/verify_import.py
	# We ship py.typed, so consumers' type checkers read these annotations. Run
	# against the installed package rather than the source tree: on the tree,
	# mypy resolves the generated `Response` to httpx's and reports thousands of
	# errors that no consumer ever sees.
	.venv-verify/bin/mypy -p incident_io
	# oasdiff compares the schema; this compares what consumers import. A
	# renamed schema, a changed operationId or a renamed path parameter is
	# `info` to oasdiff and an ImportError or TypeError to a caller.
	.venv-verify/bin/python scripts/api_surface.py check $(PACKAGE) api-surface.txt

# Accept the current surface as the new baseline. Run after a deliberate
# breaking change, alongside the major version bump.
surface: verify
	.venv-verify/bin/python scripts/api_surface.py write $(PACKAGE) api-surface.txt

clean:
	rm -rf $(PACKAGE) dist build .venv-verify .ruff_cache .mypy_cache
