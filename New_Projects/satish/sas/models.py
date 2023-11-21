from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name


class Profile(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	summary = models.TextField(max_length=2000)
	degree = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	university = models.CharField(max_length=200)
	previous_work = models.TextField(max_length=1000)
	skills  =  models.TextField(max_length=1000)