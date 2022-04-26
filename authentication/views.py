import json

import requests
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, redirect, render
from rest_framework import permissions, status
from rest_framework.views import APIView

from .serializers import UserSerializer


class authLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("Those credentials do not exist")
        login(request, user)
        accessData = json.loads(requests.post(
            f"{request.scheme}://{request.get_host()}/auth/token/obtain", data={"username": username, "password": password}).text)
        request.session['access'] = accessData['access']
        request.session['refresh'] = accessData['refresh']
        return HttpResponse("You have successfully logged in with username " + username)


class authLogout(APIView):
    def post(self, request):
        del request.session['access']
        del request.session['refresh']
        logout(request)
        return HttpResponse("You have been Logged Out.")


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return HttpResponse("User Created.")
        else:
            return HttpResponse("Error")
