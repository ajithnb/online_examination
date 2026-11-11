from rest_framework import serializers
from repository.models import questiondb

class questionserialzer(serializers.Serializer):
    question = serializers.CharField(max_length=100)
    option_a = serializers.CharField(max_length=100)
    option_b = serializers.CharField(max_length=100)
    option_c = serializers.CharField(max_length=100)
    option_d = serializers.CharField(max_length=100)
    correct_answer = serializers.CharField(max_length=100)

class SubmissionSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=100)
    question_id = serializers.PrimaryKeyRelatedField(
        queryset=questiondb.objects.all()
    )
    selected_answer = serializers.CharField(max_length=20)
    submitted_at = serializers.DateTimeField(read_only=True)

class SubmissionSerializer(serializers.Serializer):
    question_id=serializers.IntegerField()
    points=serializers.IntegerField()
    owner=serializers.CharField()
    submission_date=serializers.DateTimeField(read_only=True)
    remarks=serializers.CharField()

    def validate(self, validated_data):
        question_id=validated_data.get("question_id")
        if not Questions.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exit")
        return validated_data