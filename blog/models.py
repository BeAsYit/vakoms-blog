from django.db import models
# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey('blog.Blog', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    parent_id = models.IntegerField(null=True)

    def __str__(self):
        return self.text
