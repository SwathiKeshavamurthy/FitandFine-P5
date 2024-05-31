from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment


class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.post = Post.objects.create(
            owner=self.user,
            title='Test Post',
            content='Test content'
        )

    def test_create_comment(self):
        comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Test comment'
        )
        retrieved_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(comment, retrieved_comment)

    def test_comment_association_with_user(self):
        comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Test comment'
        )
        self.assertEqual(comment.owner, self.user)

    def test_comment_association_with_post(self):
        comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Test comment'
        )
        self.assertEqual(comment.post, self.post)

    def test_comment_content(self):
        comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Test comment'
        )
        self.assertEqual(comment.content, 'Test comment')

    def test_comment_ordering(self):
        comment1 = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Comment 1'
        )
        comment2 = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Comment 2'
        )
        comment3 = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Comment 3'
        )
        comments = Comment.objects.all()
        self.assertEqual(comments[0], comment3)
        self.assertEqual(comments[1], comment2)
        self.assertEqual(comments[2], comment1)
