from django.urls import path
from . import views
from .views import submit_callback_form

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-callback-form/', submit_callback_form, name='submit_callback_form'),
]
