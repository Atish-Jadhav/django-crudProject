"""
URL configuration for crudProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from crudApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Name for dashboard and form is necessary if you need to redirect.
    # Or the edit or delete segements will get added to the url and it will show page not found
    path('dashboard/', views.dashboard, name = 'dashboard'), 
    path('form/', views.form, name = 'form'),
    # Name property used in delete and update because we don't want url to get added like this - dashboard/delete/1/delete/2
    # Rather the url needs to be cleaned for every request - /delete/1 and /delete/2
    # The logic is in HTML page which is carried out using {% url %} tag
    path('delete/<rid>/', views.delete, name = 'delete'), 
    path('update/<uid>/', views.edit, name = 'edit'),
]
