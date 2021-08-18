from django.db import models
import re
# Create your models here.
class userManagerName(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) <= 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) <= 2:
            errors["last_name"] = "last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = ("Invalid email address")
        if len(postData['password']) < 8:
            errors["password"] = 'passowrd needs at least 8 character'
        if postData['password_cf'] != postData['password']:
            errors["password confirm"] = "password should be the same"
        
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password_cf = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManagerName()