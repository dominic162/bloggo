from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class blog(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    written_by=models.ForeignKey('writer',on_delete=models.CASCADE)
    slug=models.SlugField()
    image=models.ImageField(upload_to="images/" , default='default_blog.jpg')
    tags=TaggableManager()

    def __str__(self):
        return self.title

class writer(models.Model):
    name=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    slug=models.SlugField()
    user_image=models.ImageField(upload_to="userimage/",default='default_profile.jpg')

    def __str__(self):
        return self.name

class contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.subject
