from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        app_label = 'mysite'
        model=Us
        fields="__all__"