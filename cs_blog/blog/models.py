from django.db import models

# Create your models here.
class Post(models.Model):
    author=models.CharField(max_length=200)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=300)
    timestamp=models.DateTimeField(blank=True)
    slug=models.CharField(max_length=100)

    def __str__(self):
        return self.title +' '+self.author
class Comment(models.Model):
    slug=models.CharField(max_length=100)
    comment=models.TextField(max_length=300)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.slug +' '+self.name


