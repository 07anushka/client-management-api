from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from clients.models import Client


class ClientAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="anushka",
            email="anushka@gmail.com",
            password="Test@12345"
        )

        login = self.client.post(
            "/api/accounts/login/",
            {
                "username": "anushka",
                "password": "Test@12345"
            },
            format="json"
        )

        self.token = login.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        self.client_data = {
            "company_name": "OpenAI",
            "client_name": "Sam Altman",
            "email": "sam@openai.com",
            "phone": "9876543210",
            "website": "https://openai.com",
            "gst_number": "GST123456",
            "address": "California",
            "city": "San Francisco",
            "state": "California",
            "country": "USA",
            "status": "active"
        }

    def test_create_client(self):
        response = self.client.post(
            "/api/clients/",
            self.client_data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Client.objects.count(),
            1
        )

    def test_list_clients(self):
        Client.objects.create(
            company_name="Google",
            client_name="Sundar Pichai",
            email="google@gmail.com",
            phone="9999999999",
            address="USA",
            city="California",
            state="California",
            country="USA",
            status="active",
            created_by=self.user,
            updated_by=self.user
        )

        response = self.client.get("/api/clients/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_client(self):
        client = Client.objects.create(
            company_name="Microsoft",
            client_name="Satya Nadella",
            email="microsoft@gmail.com",
            phone="8888888888",
            address="USA",
            city="Washington",
            state="Washington",
            country="USA",
            status="active",
            created_by=self.user,
            updated_by=self.user
        )

        response = self.client.get(
            f"/api/clients/{client.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["company_name"],
            "Microsoft"
        )