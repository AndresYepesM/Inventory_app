from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
    

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'), 

    re_path('inventory/', include('product.urls')),
]
