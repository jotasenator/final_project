from django.contrib.auth.models import User
from django.test import Client, TestCase
from capstone.models import User, Issue
from datetime import timedelta
from django.utils import timezone


class SubmitIssueTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

    def test_submit_issue(self):
        response = self.client.post(
            "/submit_issue", {"issue": "Test Issue", "description": "Test Description"}
        )
        self.assertRedirects(response, "/")
        issue = Issue.objects.get(issue="Test Issue")
        self.assertEqual(issue.description, "Test Description")
        self.assertEqual(issue.user, self.user)

        # Test if the created_at field was set correctly
        now = timezone.now()
        self.assertLessEqual(issue.created_at, now)
        self.assertGreaterEqual(issue.created_at, now - timedelta(seconds=1))
