from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='profiles/', default='profiles/user-default.png')
    website = models.CharField(max_length=200, blank=True, null=True)
    gender = models.ForeignKey('Gender',  on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save_profile(self):
        '''
        Method that saves the Profile object
        '''
        self.save()

    @classmethod
    def update_profile(cls, record_id, update_value):
        '''
        Method that Updates a profile record
        '''
        cls.objects.filter(id=record_id).update(name=update_value)


class Tag(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Gender(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
