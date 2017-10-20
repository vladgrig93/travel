from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.
from django.db import models
import bcrypt

class UsersManager(models.Manager):
    def validator(self, postData):
        errors={}#no errors
        if len(postData['name'])<3 or len(postData['username'])<3:
            errors['name_error']='Name and username must be at least 3 characters long'
        if len(postData['password'])<8 or len(postData['confirm_password'])<8:
            errors['pass_length']='Password must be 8 or more characters long'
        if postData['password']!=postData['confirm_password']:
            errors['passmatch']="Passwords don't match"
        if Users.objects.filter(username=postData['username']):
            errors['exists']='This username is already taken, please try another'
        return errors
    def login_model(self, postData):
        errors={}
        user_to_check=Users.objects.filter(username=postData['username'])
        if len(user_to_check)>0:
            user_to_check=user_to_check[0]
            if bcrypt.checkpw(postData['password'].encode(), user_to_check.password.encode()):
                user={'user':user_to_check}
                return user
            else:
                errors={'error': "Invalid Login"}
                return errors
        else:
            errors={'error': "Invalid Login"}
            return errors
# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UsersManager()

class TripsManager(models.Manager):
    def trip_validator(self, postData):
        errors={}#no errors
        if len(postData['description'])<1 or len(postData['destination'])<1:
            errors['name_blank']='A field cannot be left blank'
        if str(postData['start'])<str(date.today()):
            errors['past_date']="A selected date can't be in the past"
        if str(postData['end'])<str(postData['start']):
            errors['dates']="Travel to can't be before Travel from date"
        # if Trips.objects.filter(joiners=request.session['name']):
        #     errors['exists']='You have already joined this trip'
        return errors

class Trips(models.Model):
    destination=models.CharField(max_length=255)
    description=models.TextField()
    start=models.DateField()
    end=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(Users, related_name = "trips")
    joiners=models.ManyToManyField(Users, related_name = "jtrips")
    objects=TripsManager()


    