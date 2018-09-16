from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import viewsets

from human.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    UserModel = get_user_model()
    queryset = UserModel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
