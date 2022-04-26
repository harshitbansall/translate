from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import UserCreate, authLogin, authLogout

urlpatterns = [
    path('token/obtain', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('login', authLogin.as_view(), name='login'),
    path('logout', authLogout.as_view(), name='login'),
    path('signup', UserCreate.as_view(), name='userCreate'),
]
