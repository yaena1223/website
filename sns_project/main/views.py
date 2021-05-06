from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/index.html')

def like(request):
    return render(request,'main/like.html')


def experience(request):
    return render(request,'main/experience.html')