from django.db import models

# Create your models here.

class User(models.Model):
    username = models.TextField()
    tglogin = models.TextField()
    email = models.TextField()
    avatarId = models.IntegerField()
    iq = models.IntegerField()

    def __str__(self):
        return self.username

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"Comment by {self.author.username}"

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    timestamp = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        Comment,
        blank=True
    )

    def __str__(self):
        return f"Post by {self.author.username}"
