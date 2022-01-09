from django.shortcuts import render
from . import forms
# .--> current working directory

def Studentregisterview(request):
    form=forms.StudentRegister()
    return render(request,'testApp/register.html',{'form':form})
