from django.urls import path
from friendindeed import views

app_name = 'friendindeed'

urlpatterns = [

    path('', views.index, name='index'),
    path('allusers/', views.allusers, name='allusers'),
    path('userdashboard/<slug:slug>', views.userdashboard, name='userdashboard'),
	path('userfriend/', views.userfriend, name='userfriend'),
	path('checkmessages/', views.checkmessages, name='checkmessages'),

]
