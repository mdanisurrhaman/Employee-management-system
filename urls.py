from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [
    path('home/', views.home),
    path('index/', views.index),
    path('getdata/',views.getdata, name='getdata'),
    path('about/', views.about),
    path('addData/', views.addData,name='addData'),
    path('updateData/<int:id>',views.updateData,name='updateData'),
    path('Delete/<int:id>',views.Delete,name='Delete'),

    path('Students/',views.Students,name='Students'),
    path('Addstudent/', views.Addstudent, name='Addstudent'),
    path('updatestudent/<int:id>/', views.updatestudent, name='updatestudent'),
    path('deletes/<int:id>/', views.deletes, name='deletes'),
    path('contact/', views.contact,name='contact'),
    path('register/',views.register),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')


]