from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshSlidingView, TokenObtainSlidingView

from .views import RegisterView

urlpatterns = [
    path('', TokenObtainSlidingView.as_view()),
    path('/refresh', TokenRefreshSlidingView.as_view()),
    path('/register', RegisterView.as_view())
]
