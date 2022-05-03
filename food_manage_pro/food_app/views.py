from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

def event(request):
    return render(request, 'event.html')


def contact(request):
    return render(request, 'contact.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['name']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                return redirect('adminhome')
                error = "no"
            else:
                error ="yes"
        except:
            error = "yes"
    return render(request,'admin_login.html', locals())

def user_login(request):
    return render(request, 'user_login.html')

def admin_home(request):
    return render(request, 'adminhome.html')

def signout(request):
    logout(request)
    return redirect('home')

def register(request):
    return render(request, 'user_login.html')