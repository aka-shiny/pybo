from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import generic

from pybo.forms.answer import AnswerForm
from pybo.forms.question import QuestionForm
from pybo.models import Answer, Question


class QuestionListView(generic.ListView[Question]):
    model = Question
    template_name = "question/question_list.html"
    paginate_by = 15

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

    def get_object(self, queryset: QuerySet[Question, Question] = None) -> object:
        question = get_object_or_404(Question, pk=self.kwargs.get("pk"))
        return question


class QuestionCreate(generic.CreateView[Question, QuestionForm]):
    form_class = QuestionForm
    template_name = "question/question_form.html"
    success_url = "/pybo/"


class AnswerCreateView(generic.CreateView[Answer, AnswerForm]):
    model = Answer
    form_class = AnswerForm
    template_name = "question/question_detail.html"
    success_url = "/pybo/"

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        question = get_object_or_404(Question, pk=self.kwargs.get("question_id"))
        form = self.form_class(request.POST)
        context = {"question": question, "form": form}
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("pybo:question_detail", question.id)
        else:
            return render(request, self.template_name, context)
