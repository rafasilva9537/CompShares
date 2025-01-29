from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=True, default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="", blank=True, default="") # TODO: create image directories
    text = models.TextField() # markdown text
    tags = models.ManyToManyField(Tag, through="Tag_In_Post")
    users_reactions = models.ManyToManyField(
        User, 
        through="Post_Reaction",
        related_name="post_user_reactions",
    )
    
    def __str__(self):
        return self.title
        
class Tag_In_Post(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint("post", "tag", name="unique_tag_in_post")
            ]
        
    def __str__(self):
        return f"Tag {self.tag} in {self.post.title}"

class Post_Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint("post", "user", name="unique_post_reaction")
        ]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    responded_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, default=None)
    text = models.CharField(max_length=5000)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    users_reactions = models.ManyToManyField(
        User, 
        through="Comment_Reaction",
        related_name="comment_user_reactions",
    )

    def __str__(self):
        return self.text[:51] + "..."

class Comment_Reaction(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint("comment", "user", name="unique_comment_reaction")
        ]

class Saved_Post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint("post", "user", name="unique_saved_post")
        ]

    def __str__(self):
        if self.post:
            return self.post.title
        return "Post deleted"