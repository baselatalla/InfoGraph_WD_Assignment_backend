from rest_framework import serializers 
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_flex_fields import FlexFieldsModelSerializer

from .models import  Maintenance_request , User, Image

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    photo = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )
    class Meta:
        model = User
        fields = ('id','username','email', 'first_name', 'last_name', 'password', 'photo',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name','image',]


class MRsSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.user.username
    username = serializers.SerializerMethodField()
    image = ImageSerializer(many=True)
    class Meta:
        fields = ('id' ,'user', 'username','vehicle_name','image','category','status','discerption','created_at',)
        model = Maintenance_request
        expandable_fields = {
            'image': ('ANYVEHICLE.ImageSerializer', {'many': True}),
        }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        return token
