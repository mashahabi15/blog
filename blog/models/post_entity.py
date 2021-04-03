from datetime import datetime

from django.db import models


class PostEntity(models.Model):
    user = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT, null=False, related_name='posts')
    title = models.CharField(max_length=25, null=False, blank=False)
    body = models.CharField(max_length=2048, null=False, blank=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    class Meta:
        db_table = "post_entity"

        verbose_name_plural = "post_entities"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = 1
        self.deletion_time = datetime.now()
        self.save()

    def check_post_permission(self, user_id):
        if self.user_id == user_id:
            return True
        else:
            return False
