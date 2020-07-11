from django.contrib import admin
from myapp1.models import *
# Register your models here.
my_models=[branch_model,profile]
admin.site.register(my_models)
