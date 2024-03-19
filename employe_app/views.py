from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import employeSerializer
from rest_framework.response import Response
from .models import Employe_tb
from rest_framework import status

class Employeview(APIView):
    def post(self,request):
        serializer = employeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'error','data':serializer.data},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,id=None):
        if id:
            employe = Employe_tb.objects.get(id=id)
            serializer = employeSerializer(employe)
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        employe = Employe_tb.objects.all()
        serializer = employeSerializer(employe,many=True)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    
    def patch(self,request,id=None):
        employe = Employe_tb.objects.get(id=id)
        serializer = employeSerializer(employe,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.data},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id=None):
        employe=Employe_tb.objects.get(id=id)
        employe.delete()
        return Response({'status':'success','message':'employer deleted succesfully'},status=status.HTTP_200_OK)
        

# Create your views here.
