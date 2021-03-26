from django.urls import path, include

urlpatterns = [
    path('/users', include('apps.users.urls')),
    path('/auth', include('apps.auth_.urls'))
]
