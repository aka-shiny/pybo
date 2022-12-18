from django.contrib import admin
from django.urls import include, path

from pybo.views import QuestionListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include("pybo.urls")),
    path("common/", include("common.urls")),
    path("", QuestionListView.as_view(), name="index"),
]
