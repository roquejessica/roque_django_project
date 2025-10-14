from django.shortcuts import render
from students.models import Student
from api.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def studentView(request):
    if(request.method == 'GET'):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(students, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)