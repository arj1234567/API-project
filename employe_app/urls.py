
from django.urls import path
from .views import Employeview

urlpatterns = [
    path('employe/',Employeview.as_view()),
    path('employe/<int:id>',Employeview.as_view()),
    
]
