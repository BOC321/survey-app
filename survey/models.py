from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='banners/', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='categories')

class Question(models.Model):
    text = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')

class Answer(models.Model):
    text = models.CharField(max_length=200)
    value = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

class ScoreRange(models.Model):
    min_score = models.IntegerField()
    max_score = models.IntegerField()
    color = models.CharField(max_length=20)
    description = models.TextField()

class UserResponse(models.Model):
    user_id = models.CharField(max_length=100)  # Or link to a User model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
