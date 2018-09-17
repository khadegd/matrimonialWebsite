from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import permissions, viewsets

from human.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    UserModel = get_user_model()
    queryset = UserModel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
