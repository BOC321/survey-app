from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, CategoryViewSet, QuestionViewSet, AnswerViewSet, UserResponseViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'responses', UserResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('survey.urls')),
]
