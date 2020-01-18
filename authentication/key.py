from urllib.parse import urljoin

from .http import RequestsTransport


def get_public_key(base_uri: str):
    uri = urljoin(base_uri, '/public_key.json')
    headers = {}
    client = RequestsTransport()
    return client.get(uri=uri, headers=headers)
