from django.urls import path

from pybo.views import (
    AnswerCreateView,
    QuestionCreate,
    QuestionDetailView,
    QuestionListView,
)

app_name = "pybo"

urlpatterns = [
    path("", QuestionListView.as_view(), name="index"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
    path(
        "answer/create/<int:question_id>/",
        AnswerCreateView.as_view(),
        name="answer_create",
    ),
    path("question/create/", QuestionCreate.as_view(), name="question_create"),
]
