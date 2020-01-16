# TEST CREATED USER

from django.test import TestCase
# IMPORT GET USER HELPER FUNCTION THAT COMES WITH DJANGO
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """TEST CREATING A NEW USER WITH AN EMAIL IS SUCCESSFUL"""
        email = 'test@london.com'
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_email_normalized(self):
        """THE EMAIL FOR THE NEW USER IS NORMALIZED"""
        email = 'test@LONDON.COM'
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())    
    
    def test_new_user_invalid_email(self):
        """TEST CREATING USER WITH NO EMAIL RAISES ERROR"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """TEST CREATING A NEW SUPER USER"""
        user = get_user_model().objects.create_superuser(
            'test@londonapdev.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)