from django.urls import path
from .views import home,students

urlpatterns = [
    path('', home),
    path('students/', students)
]