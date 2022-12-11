from django.urls import path

from .views import QuestionListModelView, QuestionUpdateModelView

urlpatterns = [
    path("", QuestionListModelView.as_view()),
    path("<int:pk>/edit", QuestionUpdateModelView.as_view(), name="question_edit")
]
