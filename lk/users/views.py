from rest_framework import viewsets, permissions, exceptions, status
from .serializers import CustomUserSerializer, ProfileCustomUserSerializer
from django.contrib.auth import get_user_model


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
