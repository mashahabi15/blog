from datetime import datetime
from django.db import models

from blog.enums import ScoreType


class TrendEntity(models.Model):
    score_type = models.IntegerField(choices=ScoreType.choices(), blank=True, default=None)
    post = models.ForeignKey('blog.PostEntity', on_delete=models.CASCADE, null=False, related_name='post_trends')
    comment = models.ForeignKey('blog.CommentEntity', on_delete=models.CASCADE, null=True,
                                related_name='comment_trends')
    user = models.ForeignKey('identity.UserEntity', on_delete=models.CASCADE, null=False, related_name='user_trends')

    class Meta:
        db_table = "trend_entity"

        verbose_name_plural = "trend_entities"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = 1
        self.deletion_time = datetime.now()
        self.save()

    def check_if_user_liked_or_disliked_before(self, user_id, post_id, comment_id):
        """

        :param user_id:
        :param post_id:
        :param comment_id:
        :return: This function checks if this user has liked or disliked the post or comment.
        """

        if TrendEntity.objects.filter(user_id=user_id, post_id=post_id, comment_id=comment_id).exists():
            return True

        return False
