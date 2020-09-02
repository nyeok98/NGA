from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account.views import(
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
