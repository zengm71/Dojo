from django.db import models
from datetime import date, datetime
# Create your models here.
class showManagerName(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <= 2:
            errors["name"] = "show title should be at least 2 characters"
        return errors

class showManagerDesc(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if (len(postData['desc']) < 15) or (len(postData['desc']) == 0):
            errors["desc"] = "description should be more than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManagerName()

class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True, related_name='desc')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManagerDesc()

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)