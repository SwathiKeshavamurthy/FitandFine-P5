from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Challenge
from datetime import date

User = get_user_model()

class ChallengeModelTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        # Create a challenge
        self.challenge = Challenge.objects.create(
            owner=self.user,
            title='New Year Run',
            description='Run into the new year with a 5k!',
            start_date=date.today(),
            end_date=date.today(),
            sport='running'
        )

    def test_challenge_creation(self):
        self.assertIsNotNone(self.challenge)
        self.assertEqual(Challenge.objects.count(), 1)

    def test_challenge_associated_with_user(self):
        self.assertEqual(self.challenge.owner, self.user)

    def test_default_field_values(self):
        # Assuming the image and other fields might have defaults
        self.assertEqual(self.challenge.title, 'New Year Run')
        self.assertEqual(self.challenge.sport, 'running')

    def test_retrieve_challenge_by_user(self):
        retrieved_challenge = Challenge.objects.get(owner=self.user)
        self.assertEqual(retrieved_challenge, self.challenge)

    def test_update_challenge_fields(self):
        self.challenge.title = 'Spring Marathon'
        self.challenge.description = 'A challenging marathon to start the spring.'
        self.challenge.sport = 'running'  # Update to different sport if needed
        self.challenge.save()
        updated_challenge = Challenge.objects.get(id=self.challenge.id)
        self.assertEqual(updated_challenge.title, 'Spring Marathon')
        self.assertEqual(
            updated_challenge.description,
            'A challenging marathon to start the spring.'
        )
