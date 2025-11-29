from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    due_date = serializers.DateField(required=False, allow_null=True)
    importance = serializers.IntegerField(min_value=1, max_value=10)
    estimated_hours = serializers.FloatField(min_value=0)
