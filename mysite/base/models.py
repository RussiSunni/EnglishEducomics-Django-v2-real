from django.db import models

# Create your models here.


class Stages(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=64)
    familiar = models.CharField(max_length=64)


class UserStages(models.Model):
    stageid = models.ForeignKey(Stages, on_delete=models.CASCADE)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    iscompleted = models.BooleanField

    def __str__(self):
        return self.stageid + " " + self.userid + " " + self.iscompleted
