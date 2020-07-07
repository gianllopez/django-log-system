from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('main')
        else:
            return render(
                request=request, 
                template_name='login.html', 
                context={
                    'login_error' : 'Credenciales incorrectas, si no tienes cuenta regístrate.'
                    }
            )
    return render(request=request, template_name='login.html')