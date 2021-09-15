from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    post_image = models.ImageField(upload_to='posts/')
    tag = models.ForeignKey(
        'Tag', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save_post(self):
        '''
        Method that saves the Post object
        '''
        self.save()

    @classmethod
    def update_post(cls, record_id, update_value):
        '''
        Method that Updates a post record
        '''
        cls.objects.filter(pk=record_id).update(title=update_value)

    @classmethod
    def delete_post(cls, post_id):
        '''
        Method that deletes a post
        '''
        post = cls.objects.filter(id=post_id)
        post.delete()

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save_tag(self):
        '''
        Method that saves the Tag object
        '''
        self.save()

    @classmethod
    def update_tag(cls, record_id, update_value):
        '''
        Method that Updates a tag record
        '''
        cls.objects.filter(pk=record_id).update(name=update_value)

    @classmethod
    def delete_tag(cls, tag_id):
        '''
        Method that deletes a tag
        '''
        tag = cls.objects.filter(id=tag_id)
        tag.delete()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save_comment(self):
        '''
        Method that saves the Comment object
        '''
        self.save()

    @classmethod
    def update_comment(cls, record_id, update_value):
        '''
        Method that Updates a comment record
        '''
        cls.objects.filter(pk=record_id).update(comment=update_value)

    @classmethod
    def delete_comment(cls, comment_id):
        '''
        Method that deletes a comment
        '''
        comment = cls.objects.filter(id=comment_id)
        comment.delete()

    def __str__(self):
        return self.comment


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save_like(self):
        '''
        Method that saves the Like object
        '''
        self.save()

    @classmethod
    def update_like(cls, record_id, update_value):
        '''
        Method that Updates a like record
        '''
        cls.objects.filter(id=record_id).update(post=update_value)

    @classmethod
    def delete_like(cls, like_id):
        '''
        Method that deletes a like
        '''
        like = cls.objects.filter(id=like_id)
        like.delete()

    def __str__(self):
        return self.post.id


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="following")
    followee = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="followers")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save_follow(self):
        '''
        Method that saves the Follow object
        '''
        self.save()
    
    @classmethod
    def delete_follow(cls, follow_id):
        '''
        Method that deletes a follow
        '''
        follow = cls.objects.filter(id=follow_id)
        follow.delete()