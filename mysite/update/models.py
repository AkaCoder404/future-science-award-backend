from django.db import models

# Create your models here.
class MyUser(models.Model):
    name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    contribution = models.CharField(max_length=100, null=True)
    research = models.CharField(max_length=100)

class MyUserUploads(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads', null=True)
    uploadTime = models.DateField()
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)