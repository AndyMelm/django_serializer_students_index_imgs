from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})


def myProducts(req):
    all_students = StudentSerializer(Student.objects.all(), many=True).data
    return JsonResponse(all_students, safe=False)


class MyModelView(APIView):
    
    def get(self, request):
        my_model = Student.objects.all()
        serializer = StudentSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):

        # usr =request.user
        # print(usr)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    # def put(self, request, pk):
    #     """
    #     Handle PUT requests to update an existing Task object
    #     """
    #     my_model = Student.objects.get(pk=pk)
    #     serializer = StudentSerializer(my_model, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    # def delete(self, request, pk):
    #     """
    #     Handle DELETE requests to delete a Task object
    #     """
    #     my_model = Student.objects.get(pk=pk)
    #     my_model.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
