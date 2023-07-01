from django.shortcuts import render
from imageapp.serializers import ImageSerializer,UserProfileSerializerToken
from rest_framework import permissions
from rest_framework import authentication
from imageapp.models import Image
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate


# Create your views here.

from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class=ImageSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[authentication.TokenAuthentication]
    queryset=Image.objects.all()
    def get_queryset(self,request):
        return Image.objects.filter(user=request.user)




class UserLoginapiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

            
        
    
    
