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
	# Committed too, but recreated here because generate removes the package
	# first. Without it type checkers ignore every annotation in the SDK.
	touch $(PACKAGE)/py.typed

# Python has no compile step, so we install the wheel and exercise it. See
# scripts/verify_import.py for why importing the package alone isn't enough.
verify:
	uv build
	uv venv --clear .venv-verify
	uv pip install --quiet --python .venv-verify dist/*.whl
	.venv-verify/bin/python scripts/verify_import.py

clean:
	rm -rf $(PACKAGE) dist build .venv-verify .ruff_cache
