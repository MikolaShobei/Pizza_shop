from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators as v

# Create your models here.
from apps.user_profile.services import avatar_upload
from enums import REGEXP_NAME

UserModel = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20, validators=[
        v.RegexValidator(REGEXP_NAME, 'Only alpha, min 2 max 20 ch')
    ])
    surname = models.CharField(max_length=20, validators=[
        v.RegexValidator(REGEXP_NAME, 'Only alpha, min 2 max 20 ch')
    ])
    age = models.IntegerField(validators=[
        v.MinValueValidator(10),
        v.MaxValueValidator(130)
    ])
    avatar = models.ImageField(upload_to=avatar_upload)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
