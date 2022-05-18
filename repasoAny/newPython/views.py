import random
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):

    caracters = list('abcdefghijklmnopqrstuvwxyz')
    genera_password = ''

    number = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        caracters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        caracters.extend(list('!@#$%&*()'))

    if request.GET.get('numbers'):
        caracters.extend(list('0123456789'))

    for e in range(number):
        genera_password += random.choice(caracters)

    return render(request, 'password.html', {'password': genera_password})