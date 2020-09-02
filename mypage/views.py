from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(request, 'mypage.html')

def profile_update(request):
    return render(request, 'profile_update.html')