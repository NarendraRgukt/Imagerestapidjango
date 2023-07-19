from rest_framework import serializers

from django.contrib.auth import authenticate,get_user_model
from imageapp.models import Image





        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'min_length':5
            }
            
        }
    def create(self,validated_data):
        '''creating the user using validating data'''
        email=validated_data['email']
        password=validated_data['password']
        user=authenticate(request=self.context.get('request'),email=email,password=password)
        if not user:
            return get_user_model().objects.create_user(**validated_data)
        else:
            raise serializers.ValidationError("Email already exists",'email exist')
    
    def update(self,instance,validated_data):
        '''updating the user'''
        password=validated_data.pop('password',None)
        user=super().update(instance,validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user
    

    # image_api/serializers.py







class UserTokenGenerationSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(style={
        'input_type':'password',
        
    },trim_whitespace=False)
    def validate(self,attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        user=authenticate(request=self.context.get('request'),username=email,password=password)
        print(user)
        if not user:
            msg="Invalid username or  password"
            raise serializers.ValidationError(msg,code="authorization")
        attrs['user']=user
        return attrs


    
    


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields="__all__"





    

 



      
