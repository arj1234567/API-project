from rest_framework import serializers
from .models import Employe_tb

class employeSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=20)
    Age = serializers.IntegerField()
    City = serializers.CharField(max_length=20)
    Salary  = serializers.IntegerField()
    
    class Meta:
        model = Employe_tb
        fields = '__all__'