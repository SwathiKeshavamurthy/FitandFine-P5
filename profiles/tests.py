from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTestCase(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        profile = Profile.objects.filter(owner=user).first()
        self.assertIsNotNone(profile)

    def test_profile_associated_with_user(self):
        user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        profile = Profile.objects.filter(owner=user).first()
        self.assertEqual(profile.owner, user)

    def test_default_field_values(self):
        user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        profile = Profile.objects.filter(owner=user).first()
        self.assertEqual(profile.name, '')
        self.assertEqual(profile.content, '')
        self.assertEqual(profile.email, '')
        self.assertIsNone(profile.birthday)

    def test_retrieve_profile_by_user_id(self):
        user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        profile = Profile.objects.get(owner=user)
        self.assertEqual(Profile.objects.get(owner=user.id), profile)

    def test_update_profile_fields(self):
        user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        profile = Profile.objects.get(owner=user)
        profile.name = 'Test User'
        profile.content = 'This is a test profile'
        profile.email = 'test@example.com'
        profile.birthday = '1990-01-01'
        profile.save()
        updated_profile = Profile.objects.get(owner=user)
        self.assertEqual(updated_profile.name, 'Test User')
        self.assertEqual(updated_profile.content, 'This is a test profile')
        self.assertEqual(updated_profile.email, 'test@example.com')
        self.assertEqual(
            updated_profile.birthday.strftime('%Y-%m-%d'), '1990-01-01'
        )
