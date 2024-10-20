from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def news(request):
    return render(request,'index.html')
def userhome(request):
    return render(request,'userhome.html')
def reg(request):
    if request.method =='POST':
        Username=request.POST.get('Username')
        email=request.POST.get('email')
        Number=request.POST.get('Number')
        gender=request.POST.get('gender')
        Address=request.POST.get('Address')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirm password')
        UserReg(Username=Username,Email=email,Number=Number,Gender=gender,Address=Address,Password=password,ConfirmPassword=cpassword).save()
        return redirect('login')
    return render(request, 'reg.html')
def login(request):
    if request.method =='POST':
        Username=request.POST.get('Username')
        password=request.POST.get('password')
        us=UserReg.objects.get(Username=Username,Password=password)
        if us:
            return redirect('userhome')
        else:
            return redirect('login')
    return render(request, 'login.html')

