from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'home'),
    path('about', views.about, name= 'about'),
    path('create', views.create, name= 'create'),
    path('task/<int:task_id>/status/<str:new_status>/',views.change_status, name='change_status')
]