from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)

QUES_CHOICE = (
    ('book', 'What Is your favorite book?'),
    ('food', 'What is your favorite food?'),
    ('city', 'What city were you born in?'),
    ('place', 'Where is your favorite place to vacation?'),
)

VEHICLE_CHOICE = (
    ('two', 'Two Wheeler'),
    ('three', 'Three Wheeler'),
    ('four', 'Four Wheeler'),

)


class Registration(AbstractUser):
    uid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(default="null")
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200, default="")
    contact_number = models.CharField(max_length=11, default="")
    # dob = models.DateField(default=datetime.date.today)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICE, default='male')
    question = models.CharField(
        max_length=10, choices=QUES_CHOICE, default='book')
    answer = models.CharField(max_length=20, default="")



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','contact_number', ]


    def __str__(self):
        return self.username
