from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class TestListLogView(APITestCase):
    url = reverse("audit_log:v2_list_log")
    fixtures = [
        "audit_log/tests/fixtures/base.json",
    ]

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
        self.assertEqual(self.url, "/api/audit-log/v2/log/")

    def test_list_without_filters_ok(self):
        response = self.client.get(path=self.url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("count", data)
        self.assertIn("results", data)

    def test_list_with_instance_filter_ok(self):
        filters = {"instance_id": 99}
        response = self.client.get(
            path=self.url,
            data=filters,
        )
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, data["count"])

    def test_list_with_author_filter_ok(self):
        filters = {"author": "other"}
        response = self.client.get(
            path=self.url,
            data=filters,
        )
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, data["count"])

    def test_list_with_created_from_filter_ok(self):
        filters = {"created_from": "2023-04-06T23:50:37.114531Z"}
        response = self.client.get(
            path=self.url,
            data=filters,
        )
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, data["count"])

    def test_list_with_created_to_filter_ok(self):
        filters = {"created_to": "2023-04-06T23:50:37.114531Z"}
        response = self.client.get(
            path=self.url,
            data=filters,
        )
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, data["count"])

    def test_paginated_ok(self):
        filters = {
            "limit": 1,
            "offset": 1,
        }
        response = self.client.get(
            path=self.url,
            data=filters,
        )
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(data["results"]))
