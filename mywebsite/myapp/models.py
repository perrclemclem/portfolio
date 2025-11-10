from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    time = models.DurationField()
    code = models.BooleanField(default=False)
    link = models.TextField(null=True, blank=True)
    #file
    picture = models.ImageField(upload_to="product", null=True, blank=True)
    specfile = models.FileField(upload_to="specfile", null=True, blank=True)

    def __str__(self):
        return self.title



class Extract(models.Model):
    name = models.CharField(max_length=200)
    type_code = models.TextField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class contactList(models.Model):
    topic = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.topic

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100, default='member')
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Action(models.Model):
    contactList = models.ForeignKey(contactList, on_delete=models.CASCADE)
    actionDetail = models.TextField()

    def __str__(self):
        return self.contactList.topic