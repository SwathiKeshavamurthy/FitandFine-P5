from django.test import TestCase
from django.contrib.auth.models import User
from .models import Follower


class FollowerModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass1')
        self.user2 = User.objects.create_user(username='user2', password='pass2')

    def test_create_follower(self):
        follower = Follower.objects.create(owner=self.user1, followed=self.user2)
        retrieved_follower = Follower.objects.get(pk=follower.pk)
        self.assertEqual(follower, retrieved_follower)

    def test_follower_association_with_owner(self):
        follower = Follower.objects.create(owner=self.user1, followed=self.user2)
        self.assertEqual(follower.owner, self.user1)

    def test_follower_association_with_followed(self):
        follower = Follower.objects.create(owner=self.user1, followed=self.user2)
        self.assertEqual(follower.followed, self.user2)

    def test_unique_follower(self):
        # Creating a follower for the first time should work
        follower1 = Follower.objects.create(owner=self.user1, followed=self.user2)
        self.assertIsNotNone(follower1)

        # Creating a follower for the same owner and followed again should fail
        with self.assertRaises(Exception):
            follower2 = Follower.objects.create(owner=self.user1, followed=self.user2)
