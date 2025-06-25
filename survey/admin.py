from django.contrib import admin
from .models import Survey, Category, Question, Answer, ScoreRange, UserResponse

admin.site.register(Survey)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ScoreRange)
admin.site.register(UserResponse)
