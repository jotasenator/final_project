# python manage.py test capstone.tests.test_models
from django.test import TestCase
from capstone.models import User, Issue


class IssueModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="testuser")
        Issue.objects.create(
            issue="Test issue", description="Test description", user=user
        )

    def test_issue_label(self):
        issue = Issue.objects.get(issue="Test issue")
        field_label = issue._meta.get_field("issue").verbose_name
        self.assertEqual(field_label, "issue")

    def test_description_label(self):
        issue = Issue.objects.get(issue="Test issue")
        field_label = issue._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_description_default(self):
        issue = Issue.objects.get(issue="Test issue")
        default_value = issue._meta.get_field("description").default
        self.assertEqual(default_value, "")
