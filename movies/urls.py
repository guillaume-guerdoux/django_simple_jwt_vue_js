from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdate.as_view()),

    path('movies/', MovieList.as_view()),
    path('movies-create/', MovieCreate.as_view()),
    path('movies/<int:pk>/', MovieRetrieveUpdate.as_view()),

]
