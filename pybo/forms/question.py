from django import forms

from pybo.models import Question


class QuestionForm(forms.ModelForm[Question]):
    class Meta:
        model = Question
        fields = "__all__"
