from django.db import models
from datetime import datetime


class CommentEntity(models.Model):
    post = models.ForeignKey('blog.PostEntity', on_delete=models.PROTECT, null=False, related_name='post_comments')
    user = models.ForeignKey('identity.UserEntity', on_delete=models.PROTECT, null=False, related_name='user_comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=2048, null=False, blank=False)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, editable=False)
    deletion_time = models.DateTimeField(blank=True, null=True,
                                         default=None, editable=False)

    class Meta:
        db_table = "comment_entity"

        verbose_name_plural = "comment_entities"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = 1
        self.deletion_time = datetime.now()
        self.save()
