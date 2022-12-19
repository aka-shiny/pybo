from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import DeletionMixin

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


class QuestionCreateView(LoginRequiredMixin, generic.CreateView[Question, QuestionForm]):
    form_class = QuestionForm
    template_name = "question/question_form.html"
    login_url = reverse_lazy("common:login")

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect("pybo:index")
        else:
            context = {"form": form}
            return render(request, self.template_name, context)


class QuestionUpdateView(LoginRequiredMixin, generic.UpdateView[Question, QuestionForm]):
    model = Question
    form_class = QuestionForm
    template_name = "question/question_form.html"
    success_url = reverse_lazy("pybo:index")

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Question, pk=kwargs.get("question_id"))
        form = self.form_class(instance=instance)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Question, pk=kwargs.get("question_id"))
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:question_detail', question.id)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


class QuestionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('pybo:index')

    def post(self, request, *args, **kwargs):
        return self.delete(kwargs.get('question_id'))


class AnswerCreateView(LoginRequiredMixin, generic.CreateView[Answer, AnswerForm]):
    model = Answer
    form_class = AnswerForm
    template_name = "question/question_detail.html"
    success_url = "/pybo/"
    login_url = reverse_lazy("common:login")

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        question = get_object_or_404(Question, pk=self.kwargs.get("question_id"))
        form = self.form_class()
        context = {"question": question, "form": form}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        question = get_object_or_404(Question, pk=self.kwargs.get("question_id"))
        form = self.form_class(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("pybo:question_detail", question.id)
        else:
            context = {"question": question, "form": form}
            return render(request, self.template_name, context)
