from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': "Let's learn Python!"},
    {'id': 2, 'name': "Design with me!"},
    {'id': 3, 'name': "Frontend Developers!"}
]
def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request):
    return render(request, 'base/room.html')