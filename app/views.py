from django.shortcuts import render,redirect

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
        print(role,email)
        return redirect('/')