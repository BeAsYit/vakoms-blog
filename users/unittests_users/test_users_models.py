"""
This is module with unittests for User
"""
from django.test import TestCase
import users.models as users


class TestModels(TestCase):
    def setUp(self):
        """
        Creating User instance for future tests
        """
        users.CustomUser.objects.create(email='something@gmail.com', username='admin', password='123456',
                                        phone='09876543')

    def test_user_creation(self):
        """
        Test if user created properly
        """
        user = users.CustomUser.objects.get(username='admin')
        self.assertEqual(user.phone, '09876543')
        self.assertEqual(user.email, 'something@gmail.com')

    def test_user_deletion(self):
        """
        Test if user deleted properly
        """
        users.CustomUser.objects.filter(username='admin').delete()
        user = users.CustomUser.objects.filter(username='admin')
        self.assertEqual(user.count(), 0)
