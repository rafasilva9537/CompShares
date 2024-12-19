from django.db import models
from accounts.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField(null=True)
    cover_image = models.ImageField(upload_to="", null=True) # TODO: create image directories
    post_text = models.TextField() # TODO: decide how to store text of posts
    tags = models.ManyToManyField(Tag, through="Tag_In_Post")
    users_reactions = models.ManyToManyField(
        User, 
        through="Post_Reaction",
        related_name="post_users_reactions", # TODO: does this make sense?
    )

    class Meta:
        db_table = "post"
        
class Tag_In_Post(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint("post", "tag", name="unique_tag_in_post")
            ]

class Post_Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField()

    class Meta:
        db_table = "post_reaction"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    responded_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=5000)
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField(null=True)
    users_reactions = models.ManyToManyField(
        User, 
        through="Comment_Reaction",
        related_name="comment_users_reactions", # TODO: does this make sense?
    )

class Comment_Reaction(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint("comment", "user", name="unique_comment_user")
        ]