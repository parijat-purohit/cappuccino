from django.urls import re_path
from espresso import views

urlpatterns = [
    re_path(r'^espresso/$', views.espresso_view),
]
