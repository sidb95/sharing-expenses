from django.urls import path
from .views import get as person_get
from .views import post as person_post


urlpatterns = [
    path('api/get-details', person_get),
    path('api/create-user', person_post)
]
