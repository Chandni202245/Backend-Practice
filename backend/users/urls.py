from django.urls import path
from .views import health_check, user_list_create
urlpatterns=[
    path('health/',health_check),
    path('users/',user_list_create)
]