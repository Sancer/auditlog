from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from product.models import Product


class TestRetrieveUpdateDestroyProductView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_name = 'testuser'
        cls.user_pass = 'securepassword'
        cls.user = User.objects.create_user(username=cls.user_name, password=cls.user_name)

    def setUp(self) -> None:
        refresh = RefreshToken.for_user(self.user)
        self.token = f'Bearer {refresh.access_token}'
        self.item = Product.objects.create(example_field1='123')

    def test_url_contract(self):
        self.assertEqual(self._get_url(pk=self.item.pk), f'/api/product/product/{self.item.pk}/')

    def test_update_ok(self):
        payload = {
            "example_field1": "4567",
            "example_field2": "2",
            "example_field3": "123",
            "example_field4": None,
            "example_field5": None,
            "example_field6": None,
            "example_field7": None,
            "example_field8": "5",
            "example_field9": None,
            "example_field10": None,
            "example_field11": None
        }
        response = self.client.put(
            headers={'Authorization': self.token},
            path=self._get_url(pk=self.item.pk),
            json=payload
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_ok(self):
        response = self.client.get(
            headers={'Authorization': self.token},
            path=self._get_url(pk=self.item.pk),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_ok(self):
        response = self.client.delete(
            headers={'Authorization': self.token},
            path=self._get_url(pk=self.item.pk),
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def _get_url(self, **kwargs):
        return reverse('product:retrieve_update_destroy_product', kwargs=kwargs)
