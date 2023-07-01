from django.test import TestCase

# Create your tests here.


from django.contrib.auth.models import get_user_model
from django.contrib.auth import authenticate

class UserProfile(TestCase):

    def test_login_admin(self):
        user=get_user_model().objects.create_superuser(email="naren@gmail.com",password="hello123")
        u=authenticate(user)
        
        



    
