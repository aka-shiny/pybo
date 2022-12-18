from django import forms

from pybo.models import Answer


class AnswerForm(forms.ModelForm[Answer]):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {
            "content": "답변내용",
        }
