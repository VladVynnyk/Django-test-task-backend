from django.db import models

# Create your models here.

class GroupOfUser(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

class CustomUser(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(GroupOfUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.username)
