import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    """
        Defines our customer user class User.
        Contains all required data for user authentication & authorisation.
        #TODO - write more info about this Model
    """

    username = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username', )

    @property
    def token(self):
        """
            Allows us to get token, using user.token, against user.generate_jwt_token()
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
            Creates JSON web-token for user authorisation,
            that contains user identifier and
            is being alive for 20 days.
        """
        dt = datetime.now() + timedelta(days=20)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
