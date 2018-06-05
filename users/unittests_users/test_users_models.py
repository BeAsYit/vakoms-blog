from django.test import TestCase
import users.models as users


class TestModels(TestCase):
    def setUp(self):
        users.CustomUser.objects.create(email='something@gmail.com', username='admin', password='123456',
                                        phone='09876543')

    def test_user_creation(self):
        user = users.CustomUser.objects.get(username='admin')
        self.assertEqual(user.phone, '09876543')
        self.assertEqual(user.email, 'something@gmail.com')

    def test_user_deletion(self):
        users.CustomUser.objects.filter(username='admin').delete()
        user = users.CustomUser.objects.filter(username='admin')
        self.assertEqual(user.count(), 0)
