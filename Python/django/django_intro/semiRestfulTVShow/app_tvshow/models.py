from django.db import models
from datetime import date, datetime
# Create your models here.
class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors["title"] = "show title should be at least 2 characters"
        if postData['title'] in show.objects.values_list('title', flat = True).distinct():
            errors["title"] = "show title must be unique"
        if len(postData['network']) < 3:
            errors["network"] = "network name should be at least 3 characters"
        if (len(postData['desc']) < 10) and (len(postData['desc']) > 0):
            errors["desc"] = "description should be at least 10 characters when present"
        if (len(postData['releaseDate']) != 10):                  
            errors["releaseDate"] = "release date should be 10 characters"
        if (datetime.strptime(postData['releaseDate'], '%Y-%m-%d').date() > date.today()):
            errors['releaseDateToday'] = "release date should be in the past"
        return errors

class show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()

