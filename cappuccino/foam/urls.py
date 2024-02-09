from django.contrib import admin
from django.urls import include, re_path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('espresso.urls')),
    re_path(r'^token/$', jwt_views.TokenObtainPairView.as_view()),
    re_path(r'^token/refresh/$', jwt_views.TokenRefreshView.as_view()),
]
