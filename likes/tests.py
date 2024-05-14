from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Like


class LikeModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(owner=self.user, title='Test Post', content='Test content')

    def test_create_like(self):
        like = Like.objects.create(owner=self.user, post=self.post)
        retrieved_like = Like.objects.get(pk=like.pk)
        self.assertEqual(like, retrieved_like)

    def test_like_association_with_user(self):
        like = Like.objects.create(owner=self.user, post=self.post)
        self.assertEqual(like.owner, self.user)

    def test_like_association_with_post(self):
        like = Like.objects.create(owner=self.user, post=self.post)
        self.assertEqual(like.post, self.post)

    def test_unique_like(self):
        # Creating a like for the first time should work
        like1 = Like.objects.create(owner=self.user, post=self.post)
        self.assertIsNotNone(like1)

        # Creating a like for the same user and post again should fail
        with self.assertRaises(Exception):
            like2 = Like.objects.create(owner=self.user, post=self.post)
