
from rest_framework import serializers
from .models import MyContact 
from .models import MYPost




class MYPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MYPost
        fields = "__all__"


class MyContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyContact
        fields = "__all__"
