from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content': ['My contact information is: ', 'nihal.mishra95@gmail.com']})