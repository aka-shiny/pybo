from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.forms.user_create_form import UserCreateForm


class UserCreateView(CreateView[User, UserCreateForm]):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy("common:login")
    template_name = "common/signup.html"
