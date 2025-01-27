from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    biography = models.CharField(max_length=200)
    folllows = models.ManyToManyField("self", through="Follow")

    def __str__(self):
        return self.username

class Follow(models.Model):
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_users")
    follower_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_users")

    class Meta:
        constraints = [
            models.UniqueConstraint("followed_user", "follower_user", name="unique_user_follows")
        ]