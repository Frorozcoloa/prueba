from jsonfield import fields
from rest_framework import serializers
from .models import Num

class NumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Num
        fields = "__all__"
    

 