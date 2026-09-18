# incident.io Python SDK

[![PyPI](https://img.shields.io/pypi/v/incident-io)](https://pypi.org/project/incident-io/)

The official Python SDK for the [incident.io](https://incident.io)
[public API](https://api-docs.incident.io/).

It is generated automatically from our published OpenAPI schema, so it always
tracks the live API — there is a function for every endpoint, and a type for
every request and response.

## Install

```bash
pip install incident-io
```

Requires Python 3.11 or later.

## Quickstart

Create an API key in your incident.io dashboard under **Settings → API keys**,
then:

```python
from incident_io import AuthenticatedClient
from incident_io.api.incidents_v2 import incidents_v2_list

client = AuthenticatedClient(
    base_url="https://api.incident.io",
    token="my-api-key",
)

result = incidents_v2_list.sync(client=client, page_size=25)
for incident in result.incidents:
    print(incident.reference, incident.name)
```

Every endpoint is a module with four functions. `sync` returns the parsed body
— but note that our error responses are typed too, so a failed request returns
an `ErrorResponse` rather than raising. `sync_detailed` returns a `Response`
carrying `status_code`, `headers` and `parsed`, which is the straightforward way
to tell the two apart:

```python
response = incidents_v2_list.sync_detailed(client=client)
if response.status_code != 200:
    raise RuntimeError(f"unexpected status {response.status_code}: {response.content}")
```

## Async

`asyncio` and `asyncio_detailed` mirror the two functions above, and share the
same client:

```python
result = await incidents_v2_list.asyncio(client=client, page_size=25)
```

## Configuration

`AuthenticatedClient` takes keyword arguments:

```python
client = AuthenticatedClient(
    base_url="https://api.incident.io",
    token="my-api-key",
    timeout=httpx.Timeout(30.0),                  # defaults to httpx's own
    headers={"User-Agent": "my-app/1.0.0"},       # identify your integration
    raise_on_unexpected_status=True,              # raise instead of returning None
    httpx_args={"proxy": "http://localhost:8080"},
)
```

Pass `raise_on_unexpected_status=True` to raise `UnexpectedStatus` on a status
the schema doesn't document, instead of returning `None`. Documented errors
still come back as an `ErrorResponse`; check `status_code` for those.

To reuse a connection pool or bring your own transport, pass
`httpx_args`, or hand the client a configured instance with
`client.set_httpx_client(...)`.

### Pagination

List endpoints are cursor-paginated. Read the next cursor from
`pagination_meta.after` and pass it back as `after`:

```python
from incident_io.types import UNSET

after = UNSET
while True:
    page = incidents_v2_list.sync(client=client, page_size=100, after=after)
    for incident in page.incidents:
        print(incident.reference, incident.name)

    if not page.pagination_meta or page.pagination_meta.after is UNSET:
        break
    after = page.pagination_meta.after
```

### Deprecated endpoints

Endpoints that incident.io has deprecated (for example the `v1` incidents and
custom fields endpoints, superseded by `v2`) remain available, but calling one
raises a `DeprecationWarning` naming the endpoint. Python hides these by
default, so run with `-W default::DeprecationWarning` to see them.

## Versioning

Releases are cut automatically whenever the API schema changes. We use
[SemVer](https://semver.org/): additive API changes bump the minor version and
backwards-compatible fixes bump the patch version. Changes that would break
existing code are never released automatically - they require a deliberate
major version.

## Support

Found a bug or missing something? Please
[open an issue](https://github.com/incident-io/sdk-python/issues). For questions
about the API itself, see the [API docs](https://api-docs.incident.io/).

Note that everything under `incident_io/` is generated - please don't send PRs
editing it directly; changes there come from the upstream schema.

## License

MIT - see [LICENSE](./LICENSE).

This SDK's generated code is produced by
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client),
which is licensed under MIT.
