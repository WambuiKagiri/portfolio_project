from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')