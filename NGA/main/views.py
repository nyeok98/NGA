from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.


def main(request):
    blogs = Blog.objects.all()
    return render(request, 'main.html', {'blogs': blogs})


def new(request):
    blogs = Blog.objects.all()
    return render(request, 'new.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})


def create(request):
    if request.method == 'POST':
        blog = Blog()  # 객체 틀 가져오기
        # if 'image' in request.FILES:
        # blog.image = request.FILES['image']
        blog.request_place = request.POST['requestplace']
        blog.meet_place_select = request.POST['meetplaceselect']
        blog.meet_place_detail = request.POST['meetplacedetail']
        blog.request_item = request.POST['requestitem']
        blog.request_detail = request.POST['requestdetail']
        blog.request_quantity = request.POST['requestquantity']
        blog.fees = request.POST['fees']
        blog.limited_time_hour = request.POST['limitiedhour']
        blog.limited_time_min = request.POST['limitiedmin']
        blog.limited_time_sec = request.POST['limitiedsec']
        blog.created_at = timezone.datetime.now()

        blog.save()  # 객체 저장하기

        return redirect('detail', blog.id)
    # 새로운 글 url 주소로 이동


def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': blog})


def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    blog.request_place = request.GET['requestplace']
    blog.meet_place_select = request.GET['meetplaceselect']
    blog.meet_place_detail = request.GET['meetplacedetail']
    blog.request_item = request.GET['requestitem']
    blog.request_detail = request.GET['requestdetail']
    blog.request_quantity = request.GET['requestquantity']
    blog.fees = request.GET['fees']
    blog.limited_time_hour = request.GET['limited_time_hour']
    blog.limited_time_min = request.GET['limited_time_min']
    blog.limited_time_sec = request.GET['limited_time_sec']
    blog.created_at = timezone.datetime.now()

    blog.save()

    return redirect('detail/' + str(blog.id))
