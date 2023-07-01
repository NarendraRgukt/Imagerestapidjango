from rest_framework import serializers
from imageapp.models import Image,UserProfile


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields="__all__"
        

class UserProfileSerializerToken(serializers.Serializer):
    class Meta:
        model=UserProfile
        fields=('email','password')
