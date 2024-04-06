from django.contrib.auth.models import BaseUserManager
import random
import string

def generate_referral_code():
    # Generate a random alphanumeric code of length 6
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class MyUserManager(BaseUserManager):
    def create_user(self, email,name,referral_code=None,password=None,password2=None):
        """
        Creates and saves a User with the given email, name, referral_code and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            referral_code=generate_referral_code(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user