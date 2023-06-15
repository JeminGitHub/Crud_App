from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.add, name='home'),
    path('delete/<int:taskid>/',views.delete, name='delete'),
    path('task/<int:task_id>/',views.display,name='display'),
    path('update/<int:id>/',views.update,name='update'),

]