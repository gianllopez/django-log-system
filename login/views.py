from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LoginLog

# Create your views here.

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            userdata = User.objects.get(username=username)
            LoginLog.objects.create(user=userdata, username=username)            
            login(request, user)
            return redirect('main')
        else:
            return render(
                request=request, 
                template_name='login.html', 
                context={'login_error' : 'Credenciales incorrectas, si no tienes cuenta regístrate.'}
            )
    return render(request=request, template_name='login.html')

@login_required(login_url='login')
def mainview(request):
    return render(request=request, template_name='main.html')