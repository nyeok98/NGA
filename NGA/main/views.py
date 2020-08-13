from django.shortcuts import render
from .models import Blog

# Create your views here.
def main(request):
    blogs = Blog.objects.all()
    return render(request, 'main.html', {'blogs':blogs})
