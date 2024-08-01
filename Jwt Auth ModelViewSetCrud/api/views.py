from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, DjangoModelPermissions
class StudentView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[SessionAuthentication]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    # permission_classes=[DjangoModelPermissions]

