from rest_framework import serializers
from .models import DataPoint

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = ['id', 'x_value', 'y_value', 'line_value', 'category', 'timestamp']
