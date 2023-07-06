from rest_framework import status
import pytest
from store.models import Collection


class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        Collection.objects.create(title='a')
