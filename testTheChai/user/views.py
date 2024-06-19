from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def userInfo(request):
    # return HttpResponse('hello this is user info')
    return render(request, 'user/userInfo.html')