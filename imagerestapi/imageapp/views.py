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
from rest_framework.parsers import MultiPartParser

from rest_framework import generics

class ImageMultiPartParser(MultiPartParser):
    media_type = 'image/*'


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class=ImageSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser,ImageMultiPartParser]
    
    
    def get_queryset(self):
        return Image.objects.all()
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        image = self.get_object()
        return FileResponse(image.image, content_type='image/jpeg')
        





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





class ItemListCreation(generics.CreateAPIView):
    serializer_class = ImageSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Image.objects.all()

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')  # Access uploaded images from request.FILES
        image_data_list = []
        
        for image in images:
            image_data_list.append({'image': image})

        serializer = self.get_serializer(data=image_data_list, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer):
        serializer.save()
    


    





    
    



            
        
    
    
