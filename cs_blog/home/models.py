from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=13)
    email=models.EmailField(max_length=20)
    content=models.TextField(max_length=2000)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'message from ' +self.name

class Image(models.Model):
    age=models.IntegerField()
    image=models.ImageField(upload_to='profile_image',blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.user
    


