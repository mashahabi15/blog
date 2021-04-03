from django.urls import path
from rest_framework import routers

from blog.views.comment_entity_view import CommentEntityView, ListCommentView
from blog.views.post_entity_view import PostEntityView, ListPostEntityView
from blog.views.trend_view import TrendView

router = routers.DefaultRouter()

urlpatterns = [
    path('post/', PostEntityView.as_view(), name='post_view'),
    path('post/show/', ListPostEntityView.as_view(), name='post_show'),

    path('comment/', CommentEntityView.as_view(), name='comment_view'),
    path('comment/show/', ListCommentView.as_view(), name='comment_show'),

    path('trend/', TrendView.as_view(), name='trend_view'),
]

urlpatterns += router.urls
