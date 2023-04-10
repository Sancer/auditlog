from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class TestListCreateProductView(APITestCase):
    url = reverse("product:list_create_product")

    @classmethod
    def setUpTestData(cls):
        username = "tim@me.com"
        password = "strongP@assword!"
        cls.user = User.objects.create_user(username, username, password)
        refresh = RefreshToken.for_user(cls.user)
        cls.token = f"Bearer {refresh.access_token}"

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

    def test_url_contract(self):
        self.assertEqual(self.url, "/api/product/product/")

    def test_create_ok(self):
        payload = {
            "title": "1",
            "description": "2",
            "example_field3": "3",
            "example_field4": None,
            "example_field5": None,
            "example_field6": None,
            "example_field7": None,
            "example_field8": "5",
            "example_field9": None,
            "example_field10": None,
            "example_field11": None,
        }
        response = self.client.post(path=self.url, json=payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_ok(self):
        response = self.client.get(
            path=self.url,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
