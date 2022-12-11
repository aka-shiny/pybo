from django import forms

from pybo.models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
