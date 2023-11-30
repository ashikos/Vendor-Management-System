import datetime
import jwt

from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from v1.accounts.serializers import auth
from v1.accounts import models as acc_models
from v1.accounts import permissions

# Create your views here.

class Signup(APIView):

    def post(self, request):
        serialiser = auth.UserSerializer(data=request.data)
        serialiser.is_valid()
        serialiser.save()
        return Response(serialiser.data)
    

class LoginView(APIView):

    @swagger_auto_schema(request_body=openapi.Schema(
    type="object",
    required=["username", "password"],
    properties={
        "username": openapi.Schema(type="string"),
        "password": openapi.Schema(type="string"),
    },
    ))

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("username or password incorrect")
        
        payload = {
            "id" : user.id,
            "exp" :  datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)    
        response.data = {
            "jwt": token
        }

        return response
    

class UserView(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):

        user = request.user

        return Response(auth.UserSerializer(user).data)


class LogoutView(APIView):

    def post(self, request):

        response = Response()
        response.delete_cookie(key="jwt")

        response.data = {
            "message": "succceessfully logged out"
        } 
        
        return response
    

        