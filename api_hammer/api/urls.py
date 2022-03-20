from django.urls import path

from .views import (
   get_code,
   authencation,
   get_list,
   get_profile,
   edit_profile
)


urlpatterns = [
   path('code/', get_code),
   path('auth/', authencation),
   path('users/', get_list),
   path('profile/<str:phone>/', get_profile),
   path('profile/<str:phone>/edit/', edit_profile)
]