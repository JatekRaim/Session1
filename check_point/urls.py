"""check_point URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from check_point_api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api_visitors', api_views.api_visitors, name='api_visitor'),
    path('api_orders', api_views.api_orders, name='api_orders'),
    path('api_sub_units', api_views.api_sub_units, name='api_sub_units'),
    path('api_targets', api_views.api_targets, name='api_targets'),
    path('api_employees', api_views.api_employees, name='api_employees')

]
