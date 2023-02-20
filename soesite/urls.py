from django.urls import path
from soesite import views
urlpatterns = [
    path('home/', views.disphomepage),
    path('resources/', views.disresources),
    path('resources/<subject_id>/', views.dissubject),
    path('resources/<subject_id>/review/', views.createreview),
]