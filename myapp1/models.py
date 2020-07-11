from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class branch_model(models.Model):
    branch_name=models.CharField(max_length=20)
    discount=models.IntegerField(default=0)
    def __str__(self):
        return self.branch_name+" "+str(self.discount) +"%"

class profile(models.Model):
    LOGIN_CHOICES = (
    (1, "Admin"),
    (2, "Staff"),
    (3, "Doctor"),

)
    phone_no=models.CharField(max_length=10)
    branch_of_user=models.ManyToManyField(branch_model)
    type=models.IntegerField(choices=LOGIN_CHOICES)
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.type)
