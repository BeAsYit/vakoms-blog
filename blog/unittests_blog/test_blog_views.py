from django.test import TestCase, Client
import blog.models as models
import users.models as users


class TestViews(TestCase):

    def setUp(self):
        users.CustomUser.objects.create(email='something@gmail.com', username='admin', password='123456',
                                        phone='09876543')
        models.Blog.objects.create(title='Blog1', author=users.CustomUser.objects.get(username='admin'))
        models.Post.objects.create(title="Post1", text='sometext', author=models.Blog.objects.get(title='Blog1'))

    def test_blog_list(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_list(self):
        response = self.client.get('/posts/'+str(models.Blog.objects.get(title='Blog1').pk)+'/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        response = self.client.get('/post/'+str(models.Post.objects.get(title='Post1').pk)+'/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_blog_new(self):
        response = self.client.get('blog/new', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_post_new(self):
        response = self.client.get('posts/'+str(models.Blog.objects.get(title='Blog1').pk)+'/postnew/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_add_comment_to_post(self):
        response = self.client.get('post/'+str(models.Post.objects.get(title='Post1').pk)+'/comment/', follow=True)
        self.assertEqual(response.status_code, 404)
