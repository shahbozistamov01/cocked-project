from django.shortcuts import render
from .survives import info_users
from .forms import UserModelForm
# Create your views here.


def index(request):
    forms = info_users()
    contex = {
        'forms': forms
    }
    return render(request, 'index.html', contex)

def register(request):
    form = UserModelForm()
    contex = {
        'forms': form
    }
    return render(request, 'register.html', contex)
