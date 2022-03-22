from django.urls import path
from . import views
# Create your Urls here.

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='image_create'),
]
