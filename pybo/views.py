from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
