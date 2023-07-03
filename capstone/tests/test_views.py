# python manage.py test capstone.tests.test_views
from django.test import TestCase, Client
from capstone.models import User, Issue
from datetime import datetime, timedelta


class SubmitIssueTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.client.force_login(self.user)

    def test_submit_issue(self):
        response = self.client.post(
            "/submit_issue/", {"issue": "Test Issue", "description": "Test Description"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

        # Test if the issue was created successfully
        issue = Issue.objects.get(issue="Test Issue", description="Test Description")
        self.assertEqual(issue.issue, "Test Issue")
        self.assertEqual(issue.description, "Test Description")
        self.assertEqual(issue.user, self.user)

        # Test if the created_at field was set correctly
        now = datetime.now()
        self.assertLessEqual(issue.created_at, now)
        self.assertGreaterEqual(issue.created_at, now - timedelta(seconds=1))
