from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User


class AccountsAPITest(APITestCase):

    def setUp(self):
        self.register_url = "/api/accounts/register/"
        self.login_url = "/api/accounts/login/"
        self.profile_url = "/api/accounts/profile/"

        self.user_data = {
            "username": "anushka",
            "first_name": "Anushka",
            "last_name": "Naik",
            "email": "anushka@example.com",
            "phone": "9876543210",
            "role": "admin",
            "password": "Test@12345"
        }

    def test_user_registration(self):
        response = self.client.post(
            self.register_url,
            self.user_data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(
            User.objects.first().username,
            "anushka"
        )

    def test_user_login(self):
        User.objects.create_user(
            username="anushka",
            email="anushka@example.com",
            password="Test@12345"
        )

        response = self.client.post(
            self.login_url,
            {
                "username": "anushka",
                "password": "Test@12345"
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_user_profile(self):
        user = User.objects.create_user(
            username="anushka",
            email="anushka@example.com",
            password="Test@12345"
        )

        login = self.client.post(
            self.login_url,
            {
                "username": "anushka",
                "password": "Test@12345"
            },
            format="json"
        )

        token = login.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "anushka")