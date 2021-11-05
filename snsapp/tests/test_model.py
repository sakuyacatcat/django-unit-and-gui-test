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


# Connectionモデルのオブジェクト生成
