from rest_framework import serializers

class ScoreSerializer(serializers.Serializer):
    student_id = serializers.CharField(max_length=20)
    scores = serializers.DictField(child=serializers.FloatField())