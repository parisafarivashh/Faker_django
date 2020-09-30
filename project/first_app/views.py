from django.shortcuts import render

# Create your views here.
from .models import User

def index(request):
    return render(request, 'index.html')

def users(request):
    user_list = User.objects.order_by('name')
    user_dict = {'users': user_list}
    return render(request, 'user.html', context=user_dict)
