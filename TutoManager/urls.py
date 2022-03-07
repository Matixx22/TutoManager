# Created by Mateusz at 01.03.2022


from django.urls import path

from . import views

app_name = 'TutoManager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit')
]
