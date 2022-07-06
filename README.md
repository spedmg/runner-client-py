runner_client
=============

This is a python API library for the Sony Pictures Runner / Compass API.  It is
intended to provide an object-oriented approach to Runner functionality.

## Installation

via pipenv:

`pipenv install -e git+https://github.com/spedmg/runner-client-py.git\#egg=runner_client`

via pip:
[WIP]

## Usage

Configure the client using env variables:

- `RUNNER_USERNAME`
- `RUNNER_PASSWORD`

Or directly:

```python
import runner_client

# Configure Runner Client.

runner_client.config.username = 'pparker'
runner_client.config.password = 'sp1d3rm@an'

response = runner_client.get_asset_item(74656)
```

## Testing

You will need [pipenv](https://pipenv.pypa.io/en/latest/) and GNU Make
installed.

Run `make install` to install test dependencies.
Run `make test` to run the tests.
