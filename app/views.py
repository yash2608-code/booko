from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def IndexPage(request):
    return render(request, "app/index.html")

def RegisterUser(request):
    if request.method == 'POST': 
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['passwd']
        profile = request.FILES['profilepic']

        user = Admin.objects.filter(Email=email)
        if len(user)>0:
            msg = "User already exist"
            return render(request, "app/index.html",{'err':msg})
        else:
            admin = Admin.objects.create(Role=role,Email=email,Password=password)
            if role == 'Seller':
                seller = Seller.objects.create(Admin=admin,Firstname=fname,Lastname=lname,Gender=gender,Profilepic=profile)
            elif role == 'User':
                user = User.objects.create(Admin=admin,Firstname=fname,Lastname=lname,Gender=gender,Profilepic=profile)
            else:
                print("Role Doesn't exist")
            return redirect('/')