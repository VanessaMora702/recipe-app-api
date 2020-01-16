from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None , **extra_fields):
        """Creates and saves a new user"""
        # EXTRA FIELDS MEANS WHEN YOU ADD EXTRA FIELDS EXAMPLE
        # ADDRESS, OR PEROSNAL IFORMATION FOR LOGIN YOU DONT HAVE TO
        # ADD IT ON THE MODEL 
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # PASSWORD HAS TO BE ENCRYPTED
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def create_superuser(self, email, password):
        """CREATES A SAVES A NEW SUPER USER"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
        """CUSTOM USER MODEL THAT SUPPORTS USING EMAIL ISTEAD OF USERNAME"""
        email = models.EmailField(max_length=255, unique=True)
        name = models.CharField(max_length=255)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)

        objects = UserManager()

        USERNAME_FIELD = 'email'