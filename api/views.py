from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import Student
from . seralizer import StudentSerializer

class StudentsModelsApiview(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    



