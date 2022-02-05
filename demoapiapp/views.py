from django.shortcuts import render

# Create your views here.
from demoapiapp.models import Employee
from demoapiapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeListView(APIView):
    def get(self,request):
        employee_list= Employee.objects.all()
        serializer = EmployeeSerializer(employee_list, many = True)
        return Response(serializer.data,status=status.HTTP_200_ok)


    def post(self,request):
        pass

    @classmethod
    def as_views(cls):
        pass