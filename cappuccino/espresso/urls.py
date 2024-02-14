from django.urls import re_path
from espresso import views

urlpatterns = [
    re_path(r'morse-entry/$', views.MorseCodeEntryView.as_view()),
    re_path(r'morse-result/(?P<task_id>[\w-]+)/$',
            views.MorseCodeResultView.as_view()),
]
