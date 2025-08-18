from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="alice", password="pwd12345")
        self.other = User.objects.create_user(username="bob", password="pwd12345")
        self.post = Post.objects.create(title="Hello", content="World", author=self.author)

    def test_list_public(self):
        res = self.client.get(reverse("post-list"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Hello")

    def test_detail_public(self):
        res = self.client.get(reverse("post-detail", args=[self.post.pk]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "World")

    def test_create_requires_login(self):
        res = self.client.get(reverse("post-create"))
        self.assertEqual(res.status_code, 302)  # redirected to login

    def test_create_as_logged_in(self):
        self.client.login(username="alice", password="pwd12345")
        res = self.client.post(reverse("post-create"), {
            "title": "New Post",
            "content": "Content here"
        })
        self.assertEqual(res.status_code, 302)
        self.assertTrue(Post.objects.filter(title="New Post", author=self.author).exists())

    def test_update_only_author(self):
        # Other user cannot edit
        self.client.login(username="bob", password="pwd12345")
        res = self.client.post(reverse("post-update", args=[self.post.pk]), {
            "title": "Hacked",
            "content": "Nope"
        })
        self.assertNotEqual(res.status_code, 302)  # should be forbidden or rendered with 403
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Hello")

        # Author can edit
        self.client.login(username="alice", password="pwd12345")
        res = self.client.post(reverse("post-update", args=[self.post.pk]), {
            "title": "Updated Title",
            "content": "Updated Content"
        })
        self.assertEqual(res.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Title")

    def test_delete_only_author(self):
        # Other user cannot delete
        self.client.login(username="bob", password="pwd12345")
        res = self.client.post(reverse("post-delete", args=[self.post.pk]))
        self.assertNotEqual(res.status_code, 302)
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())

        # Author can delete
        self.client.login(username="alice", password="pwd12345")
        res = self.client.post(reverse("post-delete", args=[self.post.pk]))
        self.assertEqual(res.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
