from django.test import TestCase
from django.contrib.auth import get_user_model
# TEST CREATED USER
# IMPORT GET USER HELPER FUNCTION THAT COMES WITH DJANGO


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """TEST CREATING A NEW USER WITH AN EMAIL IS SUCCESSFUL"""
        """CREATTE THE EMAIL AND PASSWORD FOR A SECOND SO THAT THE TEST CAN RUN"""
        email = 'test@london.com'
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        """ADD SOME ASSERTIONS SO TO KNOW WHERE THE EMAIL WAS CREATED CORRECTLY"""
        self.assertEqual(user.email, email)
        """PASSWORD IS ENCRYPTED SO YOU HAVE TO USE THE CHECK PASSWORD FUNCTION"""
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