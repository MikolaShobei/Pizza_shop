from django.urls import path, include

from apps.users.views import ListUsersVIew

urlpatterns = [
    path('', ListUsersVIew.as_view())
]
