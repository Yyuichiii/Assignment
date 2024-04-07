from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import MyUser

# Test for Register api endpoint
class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        """
        Test user registration endpoint.
        """
        url = reverse('Register') 
        data = {'name': 'abc', 'email': 'abc@example.com', 'password': 'securepassword123','password2': 'securepassword123'}

        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check if user is created
        user = MyUser.objects.get(email='abc@example.com')
        self.assertEqual(user.name, 'abc')
        
        # Check if response contains expected keys
        self.assertIn('msg', response.data)
        self.assertIn('User_ID', response.data)
        self.assertIn('token', response.data)

    def test_user_registration_error(self):
        """
        Test user registration with invalid data.
        """
        url = reverse('Register')
        # Missing 'email' field to trigger validation error
        data = {'name': 'abc', 'password': 'securepassword123','password2': 'securepassword123'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)




# Test for Login api endpoint
class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = MyUser.objects.create_user(email='test@example.com', password='testpassword',name='test')

    def test_login_success(self):
        """
        Test successful user login.
        """
        url = reverse('Login') 
        data = {'email': 'test@example.com', 'password': 'testpassword'}

        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('msg', response.data)

    def test_login_failure(self):
        """
        Test user login with invalid credentials.
        """
        url = reverse('Login')
        # Wrong password to trigger authentication failure
        data = {'email': 'test@example.com', 'password': 'wrongpassword'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('msg', response.data)

# Test for Profile api endpoint
class UserProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = MyUser.objects.create_user(email='test@example.com', password='testpassword',name='test')
        self.client.force_authenticate(user=self.user)  # Authenticate the client with created user

    def test_user_profile_retrieval(self):
        """
        Test user profile retrieval.
        """
        url = reverse('Profile')  

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('email', response.data)
        self.assertIn('name', response.data)
        self.assertIn('referral_code', response.data)
        self.assertIn('points', response.data)
        self.assertIn('created_at', response.data)


# Test for Referral api endpoint
class ReferralViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = MyUser.objects.create_user(name='test', email='test@example.com', password='testpassword')
        
        self.client.force_authenticate(user=self.user)  # Authenticate the client with created user

    def test_referral_view_success(self):
        """
        Test successful retrieval of user's referral information.
        """
        url = reverse('Referral')  

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_referral_view_error(self):
        """
        Test error handling in referral view.
        """
        # Simulate unauthenticated request
        self.client.force_authenticate(user=None)

        url = reverse('Referral')
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)