from django.urls import path
from rest_framework import routers

from identity.views.signup_view import SignupView

router = routers.DefaultRouter()

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),

]

urlpatterns += router.urls
