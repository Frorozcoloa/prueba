from django.shortcuts import render

from num.models import Num
from .serializers import NumSerializer
from rest_framework import viewsets
# Create your views here.

class NumView(viewsets.ModelViewSet):
    queryset = Num.objects.all()
    serializer_class = NumSerializer
    