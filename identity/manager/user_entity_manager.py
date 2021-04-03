from django.contrib.auth.base_user import BaseUserManager

from commons.manager.base_entity_manager import BaseEntityManager


class UserEntityManager(BaseUserManager, BaseEntityManager):
    pass
