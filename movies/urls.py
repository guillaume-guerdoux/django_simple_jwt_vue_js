from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/(?P<pk>\d+)/', UserRetrieveUpdate.as_view()),

    path('movies/', MovieList.as_view()),
    path('movies-create/', MovieCreate.as_view()),
    path('movies/(?P<pk>\d+)/', MovieRetrieveUpdate.as_view()),

]
