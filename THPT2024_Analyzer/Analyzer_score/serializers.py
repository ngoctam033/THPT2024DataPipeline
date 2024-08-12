from .models import FactScores
from rest_framework import serializers

class FactScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactScores
        fields = '__all__'