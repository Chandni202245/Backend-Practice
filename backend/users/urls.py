from django.urls import path
from .views import (
    health_check,
    user_list_create,
    user_detail,
    user_list_limit_offset,
    user_list_cursor
)
urlpatterns=[
    path('health/',health_check),
    path('users/',user_list_create),
    path('users/<int:pk>/',user_detail),
    path('users/limit-offset/',user_list_limit_offset),
    path('users/cursor/',user_list_cursor),
]