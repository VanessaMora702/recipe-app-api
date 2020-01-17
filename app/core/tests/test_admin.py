from django.test import TestCase, Client 
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """CREATE AN ADMIN SO WE CAN CHANGE USER'S MODEL, UPDATE IT, DELETE OR DO ANYTHING WITH AN ADMIN ACCOUNT"""
    """SET UP FUNCTION RAN BEFORE EVERY TEST IS RAN"""
    """CONSIST ON CREATING TEST CLIENT, ADD A NEW USER THAT WE CAN TEST AND MAKE SURE USER IS LOGGED INTO CLIENTE AND 
      FINALLY WE ARE GOING TO CREATE A REGULAR USER THAT IS NOT AUTHENTICATED"""
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@londonappdev.com",
            password="password123",
            name="Test user full name"
        )

    def test_user_listed(self):
        """TEST THAT USERS ARE LISTED ON USER PAGE"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """TEEST THAT THE USER EDIT PAGE WORKS"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    