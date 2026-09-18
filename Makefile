# Pinned deliberately: this generator changes its own output in minor releases,
# which would reshape our public API. Upgrade by hand and read the diff.
OPC_VERSION := 0.29.1

PACKAGE    := incident_io
SCHEMA_URL := https://api.incident.io/v1/openapiV3.json

.PHONY: fetch generate verify clean

fetch:
	curl -sfS $(SCHEMA_URL) -o openapi.json

# --meta none keeps the generator to the package itself. Any other value has it
# write pyproject.toml and README.md too, overwriting ours.
generate: openapi.json
	rm -rf $(PACKAGE)
	uvx --from openapi-python-client==$(OPC_VERSION) openapi-python-client generate \
		--path openapi.json \
		--output-path $(PACKAGE) \
		--meta none \
		--config config.yml \
		--overwrite \
		--fail-on-warning
	python3 scripts/mark_deprecated.py openapi.json $(PACKAGE)

# Python has no compile step, so we install the wheel and import it. That at
# least runs every generated module once.
verify:
	uv build
	uv venv --clear .venv-verify
	uv pip install --quiet --python .venv-verify dist/*.whl
	.venv-verify/bin/python -c "import incident_io; from incident_io.api.incidents_v2 import incidents_v2_list; print('import ok')"

clean:
	rm -rf $(PACKAGE) dist build .venv-verify .ruff_cache
