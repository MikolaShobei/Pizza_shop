from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from apps.user_profile.serializers import ProfileSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'is_staff', 'profile')
