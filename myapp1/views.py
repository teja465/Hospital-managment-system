from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import branch_model
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:

        if request.user.profile.type==1:
            create_branch=branch_form()
            if request.method=='POST':
                #
                t=branch_form(request.POST)
                t.save()






            return render(request,'admin.html',{'create_branch':create_branch})
        elif request.user.profile.type==2:
            return render(request,'staff.html')
        else:
            return render(request,'doctor.html')


    else:
        return HttpResponse("<h1> please login </h1>")
