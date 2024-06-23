from django.urls import path
from . import views

app_name = 'firstapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.crud.savedata, name='savedata'),
    path('<int:data_id>/edit/', views.crud.editdata, name='editdata'),
    path('update/', views.crud.updatedata, name='updatedata'),
    path('<int:data_id>/deletedata/', views.crud.deletedata, name='deletedata'),
]