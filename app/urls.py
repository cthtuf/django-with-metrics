from django.urls import path

from .views import (view_with_always_200, view_with_random_code, view_with_always_500)

urlpatterns = [
    path('200', view_with_always_200),
    path('random', view_with_random_code),
    path('500', view_with_always_500),
]
