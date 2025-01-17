import pytest
from typing import Dict

from supabase_functions import (
    create_client,
    AsyncFunctionsClient,
    SyncFunctionsClient,
)


@pytest.fixture
def valid_url() -> str:
    return "https://example.com"


@pytest.fixture
def valid_headers() -> Dict[str, str]:
    return {"Authorization": "Bearer test_token", "Content-Type": "application/json"}


def test_create_async_client(valid_url, valid_headers):
    # Test creating async client with explicit verify=True
    client = create_client(
        url=valid_url, headers=valid_headers, is_async=True, verify=True
    )

    assert isinstance(client, AsyncFunctionsClient)
    assert client.url == valid_url
    assert all(client.headers[key] == value for key, value in valid_headers.items())


def test_create_sync_client(valid_url, valid_headers):
    # Test creating sync client with explicit verify=True
    client = create_client(
        url=valid_url, headers=valid_headers, is_async=False, verify=True
    )

    assert isinstance(client, SyncFunctionsClient)
    assert client.url == valid_url
    assert all(client.headers[key] == value for key, value in valid_headers.items())


def test_type_hints():
    from typing import get_type_hints, Union

    hints = get_type_hints(create_client)

    assert hints["url"] == str
    assert hints["headers"] == dict[str, str]
    assert hints["is_async"] == bool
    assert hints["verify"] == bool
    assert hints["return"] == Union[AsyncFunctionsClient, SyncFunctionsClient]