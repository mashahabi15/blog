from django.db import models

from commons.base_entity_queryset import BaseEntityQuerySet


class BaseEntityManager(models.Model):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(BaseEntityManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return BaseEntityQuerySet(self.model).filter(deletion_time=None)
        return BaseEntityQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()
