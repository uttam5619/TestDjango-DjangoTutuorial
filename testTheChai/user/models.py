from django.db import models

# Create your models here.

class UserInfo(models.Model):
    
    GENDER_TYPES = [
    ('M', 'male'),
    ('F', 'female'),
    ("O", 'other'),
    ]
    EDUCATION_CHOICES = [
    ('HS', 'HighSchool'),
    ('SC', 'SecondarySchool'),
    ('UG', 'UnderGraduate'),
    ('PG', 'PostGraduate'),
    ]
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True, default=None)
    password = models.CharField(max_length=250)
    age = models.DurationField(default=None)
    dob= models.DateField(default=None)
    isAdult = models.BooleanField(default=False)
    address = models.TextField(default= None)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES, default=None)
    education = models.CharField(max_length=2, choices= EDUCATION_CHOICES, default=None)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user_name


class Orders(models.Model):
    pass

class PurchaseHistory(models.Model):
    pass

class WhishList(models.Model):
    pass

class Feeds:
    #like
    #commet
    pass