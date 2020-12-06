from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
        The custom user model that derived from AbstractUserModel
        has to override own manager. Django uses model managers
        for creating instances.
    """

    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required field')

        if not email:
            raise ValueError('Email is required field')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, username, email, password=None, **extra_fields):
        """
            Creates and returns User
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """
            Creates and returns User with admin (superuser) permissions
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must has is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must has is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)