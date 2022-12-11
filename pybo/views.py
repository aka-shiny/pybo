from typing import Any

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from pybo.forms.answer import AnswerForm
from pybo.forms.question import QuestionForm
from pybo.models import Answer, Question


class QuestionListView(generic.ListView[Question]):
    model = Question
    template_name = "question/question_list.html"

    def get_queryset(self) -> QuerySet[Question]:
        qs = super().get_queryset().order_by("-create_date")
        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, QuestionForm]:
        context = super().get_context_data()
        return context


class QuestionDetailView(generic.DetailView[Question]):
    model = Question
    context_object_name = "question"
    template_name = "question/question_detail.html"
    success_url = "/pybo/"

    def get_object(self) -> object:
        question = get_object_or_404(Question, pk=self.kwargs.get("pk"))
        return question


class QuestionCreate(generic.CreateView[Question]):
    form_class = QuestionForm
    template_name = "question/question_form.html"


class AnswerCreateView(generic.CreateView[Answer]):
    model = Answer
    form_class = AnswerForm
    template_name = "question/question_detail.html"
    success_url = "/pybo/"

    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs.get("question_id"))
        answer = Answer(
            question=question,
            content=request.POST.get("content"),
            create_date=timezone.now(),
        )
        answer.save()
        return redirect("pybo:question_detail", question.id)
