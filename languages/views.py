from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from .models import Language
from .serializers import LanguageSerializer, UserSerializer

from django.contrib.auth.models import User


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
