# yourapp/serializers.py

from rest_framework import serializers
from .models import Symphony_Counting_Model

class Symphony_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Symphony_Counting_Model
        fields = ['id', 'name', 'countedInteractions', 'isTrending']
