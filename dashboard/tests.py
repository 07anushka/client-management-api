from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User


class DashboardAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            email="admin@gmail.com",
            password="Test@12345"
        )

        login = self.client.post(
            "/api/accounts/login/",
            {
                "username": "admin",
                "password": "Test@12345"
            },
            format="json"
        )

        self.token = login.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

    def test_dashboard_api(self):
        response = self.client.get("/api/dashboard/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn("total_clients", response.data)
        self.assertIn("active_clients", response.data)
        self.assertIn("total_packages", response.data)
        self.assertIn("active_subscriptions", response.data)
        self.assertIn("total_projects", response.data)
        self.assertIn("total_revenue", response.data)