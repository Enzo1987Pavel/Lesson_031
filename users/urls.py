from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads.views import *
from avito import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", root),
    path("category/", CategoryView.as_view()),
    path("category/<int:pk>", CategoryDetailView.as_view()),
    path("ad/", AdView.as_view()),
    path("ad/<int:pk>", AdDetailView.as_view()),
    path("user/", include("users.urls"))

]
