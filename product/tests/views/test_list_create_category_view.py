from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class TestListCreateCategoryView(TestCase):
    url = reverse("product:list_create_category")

    @classmethod
    def setUpTestData(cls):
        cls.user_name = "testuser"
        cls.user_pass = "securepassword"
        cls.user = User.objects.create_user(
            username=cls.user_name, password=cls.user_pass
        )

    def setUp(self) -> None:
        refresh = RefreshToken.for_user(self.user)
        self.token = f"Bearer {refresh.access_token}"
        self.client.force_login(user=self.user)

    def test_url_contract(self):
        self.assertEqual(self.url, "/api/product/category/")

    def test_create_ok(self):
        payload = {
            "example_field1": "1",
            "example_field2": "2",
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
        response = self.client.post(
            headers={"Authorization": self.token}, path=self.url, json=payload
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_ok(self):
        response = self.client.get(
            headers={"Authorization": self.token},
            path=self.url,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
