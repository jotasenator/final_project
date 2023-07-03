# python manage.py test capstone.tests.test_urls
from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from capstone.views import (
    index,
    login_view,
    logout_view,
    register,
    submit_issue,
)
from capstone.models import User, Issue


class TestIndexViewResolution(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse("index")

        self.assertEquals(resolve(url).func, index)

    def test_login_url_is_resolved(self):
        url = reverse("login")

        self.assertEquals(resolve(url).func, login_view)

    def test_logout_url_is_resolved(self):
        url = reverse("logout")

        self.assertEquals(resolve(url).func, logout_view)

    def test_register_url_is_resolved(self):
        url = reverse("register")

        self.assertEquals(resolve(url).func, register)

    def test_submit_issue_url_is_resolved(self):
        url = reverse("submit_issue")

        self.assertEquals(resolve(url).func, submit_issue)

    def test_unknown_path_url_is_resolved(self):
        url = "/this/path/is/unreal"
        self.assertEquals(resolve(url).func, index)


class TestIndexView(TestCase):
    def setUp(self):
        # Get the custom user model
        User = get_user_model()

        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_index_url_is_resolved(self):
        url = reverse("index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "capstone/index.html")

    def test_login_url_is_resolved(self):
        url = reverse("login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "capstone/login.html")

    def test_logout_url_is_resolved(self):
        # Log in the test user
        self.client.login(username="testuser", password="testpass")

        url = reverse("logout")
        response = self.client.get(url)

        self.assertRedirects(response, "/")

    def test_register_url_is_resolved(self):
        url = reverse("register")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "capstone/register.html")

    def test_submit_issue_url(self):
        # Log in the test user
        login_successful = self.client.login(username="testuser", password="testpass")
        self.assertTrue(login_successful)

        url = reverse("submit_issue")
        response = self.client.post(
            url, {"issue": "Test issue", "description": "Test description"}
        )
        self.assertRedirects(response, reverse("index"))

    def test_unknown_path_url_is_resolved(self):
        url = "/this/path/is/unreal"
        response = self.client.get(url)

        self.assertRedirects(response, "/")
