from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UserInfo

# Create your views here.
def userList(request):
    users_information = UserInfo.objects.all()
    context = {
        'users': users_information
    }
    return render(request, 'user/userList.html', context)

def registerUser(request):
    pass

def updateUser(request):
    pass

def deleteUser(request):
    pass

def getAnUser(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    context ={
        'user': user
    }
    render(request, 'user/userDetail.html', context )