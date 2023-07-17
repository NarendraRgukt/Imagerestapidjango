from django.shortcuts import render
from imageapp.serializers import ImageSerializer
from rest_framework import permissions
from rest_framework import authentication
from imageapp.models import Image
from django.contrib.auth import get_user_model
from django.http import FileResponse

from rest_framework import status
from django.contrib.auth import login
from imageapp.serializers import UserSerializer,UserTokenGenerationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class=ImageSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    
    def get_queryset(self):
        return Image.objects.filter(user=self.request.user.id)
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        image = self.get_object()
        return FileResponse(image.image, content_type='image/jpeg')


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    


class CreateUserApiView(generics.CreateAPIView):
    '''view for creating the user'''
    serializer_class=UserSerializer






class CreateUserToken(ObtainAuthToken):
    serializer_class=UserTokenGenerationSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class UserManageApiView(generics.RetrieveUpdateAPIView):
    '''updating and retrieving the user'''
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user







    

    





    
    



            
        
    
    
