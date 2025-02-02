
from django.contrib import admin
from django.urls import path
from userapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("profile", profile, name="profile"),
    path("questions", questions, name="questions"),
    path("questions/Detail", questionDetails, name="questionDetails"),
    path("tags", tags, name="tags"),
    path("users", users, name="users"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", log_out, name="logout"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)