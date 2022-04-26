from django.urls import path

from .views import Home, Login, Projects, SaveSentence, SignUp, Translate

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('home', Home.as_view(), name='Home'),
    path('login', Login.as_view(), name='Login'),
    path('signup', SignUp.as_view(), name='Signup'),
    path('translate', Translate.as_view(), name='Home'),
    path('projects', Projects.as_view(), name='Projects'),


    path('saveSentence', SaveSentence.as_view(), name='SaveSentence'),
]
