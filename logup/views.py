from django.shortcuts import render

# Create your views here.
def logupview(request):
    return render(request, 'logup.html')