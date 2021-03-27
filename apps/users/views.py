from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from apps.user_profile.serializers import ProfileSerializer
from apps.users.permissions import IsSuperUser
from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class ListUsersVIew(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserUpToAdminView(GenericAPIView):
    permission_classes = [IsSuperUser]
    model = UserModel.objects

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUpdateProfileView(UpdateAPIView):
    serializer_class = ProfileSerializer

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_object(self):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        return user.profile
