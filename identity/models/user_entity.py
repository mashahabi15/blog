from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserEntity(AbstractUser):
    username = None
    is_staff = None
    date_joined = None
    last_login = None

    email = models.EmailField(_('email address'), blank=False, unique=True)
    password = models.CharField(_('password'), null=True, blank=True, max_length=128)

    # objects = UserEntityManager(alive_only=True)
    # objects_including_deleted = UserEntityManager(alive_only=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user_entity"

        verbose_name_plural = "user_entities"
