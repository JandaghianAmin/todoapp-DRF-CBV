from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True,related_name='todos'
    )
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = "user"

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.title[0:3]  

    def get_user(self):
        return self.title[0:3]  


