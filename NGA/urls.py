from django.contrib import admin
from django.urls import path, include
from main import views as main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', include('mypage.urls')),
    path('', include('account.urls')),

    path('', main_view.main, name="main"),
    path('detail/<int:blog_id>', main_view.detail, name="detail"),
    path('new/', main_view.new, name="new"),
    path('create/', main_view.create, name="create"),
    path('edit/<int:blog_id>', main_view.edit, name="edit"),
]