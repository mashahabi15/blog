from django.db.models import QuerySet
from django.utils import timezone


class BaseEntityQuerySet(QuerySet):
    def delete(self):
        return super(BaseEntityQuerySet, self).update(deletion_time=timezone.now())

    def hard_delete(self):
        return super(BaseEntityQuerySet, self).delete()
