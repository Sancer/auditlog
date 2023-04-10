from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from product.models import Category


class TestRetrieveUpdateDestroyCategoryView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        username = "tim@me.com"
        password = "strongP@assword!"
        cls.user = User.objects.create_user(username, username, password)
        refresh = RefreshToken.for_user(cls.user)
        cls.token = f"Bearer {refresh.access_token}"

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.item = Category.objects.create(title="123")

    def test_url_contract(self):
        self.assertEqual(
            self._get_url(pk=self.item.pk), f"/api/product/category/{self.item.pk}/"
        )

    def test_update_ok(self):
        payload = {
            "title": "4567",
            "description": "2",
            "example_field3": "123",
            "example_field4": None,
            "example_field5": None,
            "example_field6": None,
            "example_field7": None,
            "example_field8": "5",
            "example_field9": None,
            "example_field10": None,
            "example_field11": None,
        }
        response = self.client.put(
            path=self._get_url(pk=self.item.pk),
            json=payload,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_ok(self):
        response = self.client.get(
            path=self._get_url(pk=self.item.pk),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_ok(self):
        response = self.client.delete(
            path=self._get_url(pk=self.item.pk),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def _get_url(self, **kwargs):
        return reverse("product:retrieve_update_destroy_category", kwargs=kwargs)
