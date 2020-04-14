
# from django.shortcuts import render,HttpResponse,redirect
# from rest_framework import generics
# from .models import MYPost, MyContact 
# from .serializers import MYPostSerializer, MyContactSerializer 

# def index(request):
#     return render(request,'blog_api/index.html')

# viewset view Router Here

from rest_framework import viewsets
from . import models
from . import serializers 



class MyPostViewset(viewsets.ModelViewSet):
    queryset = models.MYPost.objects.all()
    serializer_class = serializers.MYPostSerializer


class MycontactViewset(viewsets.ModelViewSet):
    queryset = models.MyContact.objects.all()
    serializer_class = serializers.MyContactSerializer
