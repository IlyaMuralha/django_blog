from django.shortcuts import render


def showblog(request):
    return render(request, 'blogapp/showblog.html')
