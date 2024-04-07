from django.db import models
from .managers import MyUserManager
from django.contrib.auth.models import AbstractBaseUser

class MyUser(AbstractBaseUser):
    """
    Custom user model representing a user in the system.
    """
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
        help_text="The unique email address of the user."
    )
    name = models.CharField(max_length=200, help_text="The name of the user.")
    referral_code = models.CharField(
        max_length=6,
        unique=True,
        null=True,
        blank=True,
        help_text="A unique referral code assigned to the user."
    )
    points = models.PositiveIntegerField(
        null=True,
        default=0,
        help_text="Points representing the number of users referred"
        )
    
    referred_user = models.ManyToManyField('self',symmetrical=False)
    
    
    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether this user should be treated as active. "
                  "Unselect this instead of deleting accounts."
    )
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates whether this user has admin access."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the user was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the user was last updated."
    )

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        """
        Return a string representation of the user, which is their email address.
        """
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Check if the user has a specific permission.
        For simplicity, always return True for admin users.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Check if the user has permissions to view the app specified by `app_label`.
        For simplicity, always return True.
        """
        return True

    @property
    def is_staff(self):
        """
        Check if the user is a member of staff (admin).
        """
        return self.is_admin
