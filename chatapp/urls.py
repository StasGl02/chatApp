from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('addbro', addbro, name='addbro'),
    path('addsis', addsis, name='addsis'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
