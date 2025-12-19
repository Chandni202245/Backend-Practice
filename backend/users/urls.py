from django.urls import path
from .views import health_check, user_list_create, user_detail
urlpatterns=[
    path('health/',health_check),
    path('users/',user_list_create),
    path('users/<int:pk>/',user_detail),
]