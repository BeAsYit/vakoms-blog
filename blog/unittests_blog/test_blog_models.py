from django.test import TestCase
import blog.models as models
import users.models as users


class TestModels(TestCase):
    def setUp(self):
        users.CustomUser.objects.create(email='something@gmail.com', username='admin', password='123456',
                                        phone='09876543')
        models.Blog.objects.create(title='Blog1', author=users.CustomUser.objects.get(username='admin'))
        models.Post.objects.create(title="Post1", text='sometext', author=models.Blog.objects.get(title='Blog1'))
        models.Comment.objects.create(author='admin', text='sometext', post=models.Post.objects.get(title='Post1'))

    def test_blog_creation(self):
        blog = models.Blog.objects.get(title='Blog1')
        self.assertEqual(blog.title, 'Blog1')

    def test_post_creation(self):
        post = models.Post.objects.get(title='Post1')
        self.assertEqual(post.title, 'Post1')
        self.assertEqual(post.text, 'sometext')

    def test_comment_creation(self):
        comment = models.Comment.objects.get(author='admin')
        self.assertEqual(comment.author, 'admin')
        self.assertEqual(comment.text, 'sometext')

    def test_comment_deletion(self):
        models.Comment.objects.filter(author='admin').delete()
        comment = models.Comment.objects.filter(author='admin')
        self.assertEqual(comment.count(), 0)

    def test_post_deletion(self):
        models.Post.objects.filter(title='Post1').delete()
        post = models.Post.objects.filter(title='Post1')
        self.assertEqual(post.count(), 0)

    def test_blog_deletion(self):
        models.Blog.objects.filter(title='Blog1').delete()
        blog = models.Blog.objects.filter(title='Blog1')
        self.assertEqual(blog.count(), 0)
