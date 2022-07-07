from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .custonauth import CustomeAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomeAuthentication]
    permission_classes = [IsAuthenticated]

