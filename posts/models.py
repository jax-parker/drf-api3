from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    launch_site = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=False, blank=False)
    what3words = models.CharField(max_length=75, null=False,blank=False)
    comments = models.TextField(max_length=10000, null=False, blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_post_mhjm11', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
