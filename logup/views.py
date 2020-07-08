from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import LogUpModel

# Create your views here.

def logupview(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )
        logup = LogUpModel.objects.create(
            user=user,
            name = data['name'],
            surname = data['surname'],
            phone = data['phone'],
            age = data['age']
        )
        return redirect(to='login')
    return render(request=request, template_name='logup.html')