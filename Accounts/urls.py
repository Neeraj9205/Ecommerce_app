from django.urls import path
from .import views

urlpatterns=[
    path('',views.loadregister,name='register'),
    path('login',views.loadlogin, name='login'),
    path('reg',views.Register),
    path('userlogin',views.Login),
    path('userlogout',views.Logout,name='logout'),
    path('dashbord',views.Dashbord, name='dashbord'),
]