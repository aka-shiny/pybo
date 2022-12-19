from django.urls import path

from pybo.views import (
    AnswerCreateView,
    QuestionCreateView,
    QuestionDetailView,
    QuestionListView, QuestionUpdateView, QuestionDeleteView
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
    path("question/create/", QuestionCreateView.as_view(), name="question_create"),
    path("question/modify/<int:question_id>/", QuestionUpdateView.as_view(), name="question_modify"),
    path("question/delete/<int:question_id>", QuestionDeleteView.as_view(), name="question_delete"),
]
