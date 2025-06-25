from rest_framework import serializers
from .models import Survey, Category, Question, Answer, ScoreRange, UserResponse

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title', 'banner_image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'survey']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'category']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'value', 'question']

class ScoreRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreRange
        fields = ['id', 'min_score', 'max_score', 'color', 'description']

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['id', 'user_id', 'question', 'answer']
