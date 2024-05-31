from django.test import TestCase
from .models import About, Collaborate
from django.utils import timezone

class AboutModelTest(TestCase):

    def setUp(self):
        self.about = About.objects.create(
            title="About Us",
            content="This is the about section.",
            last_updated=timezone.now()
        )

    def test_about_creation(self):
        self.assertTrue(isinstance(self.about, About))
        self.assertEqual(self.about.__str__(), self.about.title)

    def test_about_update(self):
        old_updated_time = self.about.last_updated
        self.about.content = "Updated content"
        self.about.save()
        self.assertNotEqual(self.about.last_updated, old_updated_time)


class CollaborateModelTest(TestCase):

    def setUp(self):
        self.collaborate = Collaborate.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            message="I would like to collaborate with your team.",
            created_at=timezone.now()
        )

    def test_collaborate_creation(self):
        self.assertTrue(isinstance(self.collaborate, Collaborate))
        self.assertEqual(self.collaborate.__str__(), 
                         f"Collaboration request from {self.collaborate.name}")

    def test_collaborate_fields(self):
        self.assertEqual(self.collaborate.name, "John Doe")
        self.assertEqual(self.collaborate.email, "john.doe@example.com")
        self.assertEqual(self.collaborate.message, 
                         "I would like to collaborate with your team.")
