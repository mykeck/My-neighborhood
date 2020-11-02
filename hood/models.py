from django.db import models
from django.db.models import Q
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class neighbourhood(models.Model):
    neighbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood = neighbourhood).delete() 

class notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    # priority = models.CharField(max_length=15,choices=Priority,default="Informational")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

