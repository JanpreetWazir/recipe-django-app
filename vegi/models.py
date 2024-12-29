from django.db import models
from django.contrib.auth.models import User

class Receipe(models.Model):
    User = models.ForeignKey(User , on_delete=models.SET_NULL , null = True , blank = True)
    receipe_name = models.CharField(max_length=50)
    receipe_description = models.CharField(max_length=200)
    receipe_image = models.ImageField(upload_to="receipe")

