from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
import pytest

User = get_user_model()


@pytest.mark.usefixtures("dummy_data")
class UserAuthTestCase(APITestCase):
    username = "superuser"
    password = "superuser"

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_successful_login_gives_200(self):
        response = self.client.post(
            '/api/token/',
            {
                'username': self.username,
                'password': self.password
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)
