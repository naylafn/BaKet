import uuid
from django.db import models
# from django.contrib.auth.models import User

# TODO: Implementasi User as a Foreign Key --> setelah Auth selesai

# Posts model
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)                # By default this one is just same as created_at
    
    class Meta:
        # Order all the posts by the created_at field in descending order
        ordering = ['-created_at']
        

# Replies model
class Reply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Order all the replies by liked most and created_at, descending
        ordering = ['-like_count', '-created_at']
        
        
# Likes (relationship) model
class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, null=True)
    
    # If reply null == like for a post
