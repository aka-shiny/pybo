from typing import Any

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.views import generic

from pybo.forms.question import QuestionForm
from pybo.models import Question


class QuestionListModelView(generic.ListView[Question]):
    model = Question
    template_name = 'question/question_list.html'

    def get_queryset(self) -> QuerySet[Question]:
        qs = super().get_queryset().order_by('-create_date')
        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, QuestionForm]:
        context = super().get_context_data()
        return context


class QuestionUpdateModelView(generic.UpdateView[Question]):
    model = Question
    context_object_name = 'question'
    form_class = QuestionForm
    template_name = 'question/question_form.html'
    success_url = '/pybo/'

    def get_object(self) -> object:
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        return question
