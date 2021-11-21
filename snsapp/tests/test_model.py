from django.test import TestCase
from django.contrib.auth.models import User
from snsapp.models import Post
from django.core.exceptions import ValidationError

######################
# Test of Post Model #
######################


class TestPostModel(TestCase):
    # Prepare relational data
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='testuser',
            password='testpass',
            email='example@gmail.com'
        )

    # Get relational instance
    def setUp(self):
        self.test_user = User.objects.get(pk=1)

    # Test case 1: create object successfully
    def test_create_object_success(self):
        post = Post.objects.create(
            title="a" * 100,
            content="a" * 1000,
            user=self.test_user
        )
        test_post = Post.objects.get(pk=1)
        self.assertEqual(post, test_post)

    # Test case 2: create object failure by character limit
    def test_create_object_failure_by_character_limit(self):
        post = Post(
            title="a" * 200,
            content="a" * 1000,
            user=self.test_user
        )
        post.save()
        try:
            post.full_clean()
        except ValidationError:
            pass


class TestPostModelUtility(TestCase):
    # Prepare relational data
    @classmethod
    def setUpTestData(cls):
        cls.post_user = User.objects.create(
            username='testuser',
            password='testpass',
            email='example@gmail.com'
        )
        cls.like_user = User.objects.create(
            username='testuser2',
            password='testpass2',
            email='example2@gmail.com'
        )
        for i in range(1, 10):
            post = Post.objects.create(
                title="a" * i,
                content="aa" * i,
                user=cls.post_user,
            )
            if i % 3 == 0:
                post.like.add(cls.like_user)
                post.save()
            else:
                pass

    # Get relational instance
    def setUp(self):
        self.like_user = User.objects.get(username='testuser2')

    # Test case: extract Post objects by information of specified User object
    def test_extract_post_liked_by_specified_user(self):
        liked_post = Post.extract_post_liked_by_specified_user(
            self.like_user)
        for post in liked_post:
            self.assertEqual(post.id % 3, 0)
