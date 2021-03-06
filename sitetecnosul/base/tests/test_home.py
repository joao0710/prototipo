import pytest
from django.urls import reverse
from sitetecnosul.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200

def test_title(resp):
    assert_contains(resp, '<title>Tecnosul</title>')

