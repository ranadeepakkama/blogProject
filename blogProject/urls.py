"""
URL configuration for blogProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import blogPage,edit,page,delete,search,register_page,login_page,blog_page,edit_image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',blogPage,name='home'),
    path('page/',page,name = 'page_list'),
    path('delete/<int:id>',delete,name = 'delete'),
    path('edit/<int:id>', edit,name = 'edit'),
    path('search/',search,name = 'search'),
    path('register/',register_page,name = 'register'),
    path('',login_page,name = 'login'),
    path('logout/',login_page,name = 'logout'),
    path('blog/<int:id>',blog_page,name = 'blog_page'),
    path('editImage/<int:id>',edit_image,name = 'edit_image')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
