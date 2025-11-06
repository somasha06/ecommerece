"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from eshop.views import *
from eshop.adminview import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path("",home,name="homepage"),
    path("admin/",admindashboard,name="dashboard"),
    path("admin/managecategories",managecategories,name="managecategories"),
    path("admin/managecategories/<int:id>/delete",deletecategory,name="deletecategory"),
    # path("admin/managecategories/<int:id>/view",viewcategory,name="viewcategory"),
    path("admin/product/insert",insertproduct,name="insertproduct"),
    path("admin/product",manageproduct,name="manageproduct"),
    path("admin/product/<int:id>/delete",deleteproduct,name="deleteproduct"),
    # path("admin/product/<int:id>/view",viewproduct,name="viewproduct"),
    path("admin/product/<int:id>/edit",editproduct,name="editproduct"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
