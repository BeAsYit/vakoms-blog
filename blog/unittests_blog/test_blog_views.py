"""
This is module with unittests for blog.views
"""
from django.test import TestCase
import blog.models as models
import users.models as users


class TestViews(TestCase):

    def setUp(self):
        """
        We are making our db objects for future test
        """
        users.CustomUser.objects.create(email='something@gmail.com', username='admin', password='123456',
                                        phone='09876543')
        models.Blog.objects.create(title='Blog1', author=users.CustomUser.objects.get(username='admin'))
        models.Post.objects.create(title="Post1", text='sometext', author=models.Blog.objects.get(title='Blog1'))

    def test_blog_list(self):
        """
        Test if not logined user can see blog list
        """
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_list(self):
        """
        Test if not logined user can see post list
        """
        response = self.client.get('/posts/'+str(models.Blog.objects.get(title='Blog1').pk)+'/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        """
        Test if not logined user can see post details
        """
        response = self.client.get('/post/'+str(models.Post.objects.get(title='Post1').pk)+'/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_blog_new(self):
        """
        Test if not logined user can't make new blog
        """
        response = self.client.get('blog/new', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_post_new(self):
        """
        Test if not logined user can't make new post
        """
        response = self.client.get('posts/'+str(models.Blog.objects.get(title='Blog1').pk)+'/postnew/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_add_comment_to_post(self):
        """
        Test if not logined user can't add comments
        """
        response = self.client.get('post/'+str(models.Post.objects.get(title='Post1').pk)+'/comment/', follow=True)
        self.assertEqual(response.status_code, 404)
