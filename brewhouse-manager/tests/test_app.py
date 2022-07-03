import pytest
from app.app import create_server


def test_create_server(context):
    app = create_server(context=context)
    assert app is not None
