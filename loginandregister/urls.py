
from django.urls import path
from loginandregister import views
urlpatterns = [
    path('loginpage/', views.loginpage),
    path('registration/', views.register),
    path('forgotpassword/', views.forgotpassword),
    path('createnewuser/', views.createnewuser),
    path('loginvalidation/', views.loginvalidation),
    path('logout/', views.userlogout),
]