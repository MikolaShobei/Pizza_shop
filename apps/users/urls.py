from django.urls import path, include

from apps.users.views import ListUsersVIew, UserUpdateProfileView, UserUpToAdminView

urlpatterns = [
    path('', ListUsersVIew.as_view(), name='get_users_list'),
    path("/<int:pk>/profile/update", UserUpdateProfileView.as_view(), name='update_user_profile'),
    path('/<int:pk>/to_staff', UserUpToAdminView.as_view(), name='user_update_update_to_staff')
]
