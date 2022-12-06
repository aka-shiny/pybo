# pybo

### 규칙
1. poetry를 사용한다
2. 점프 투 장고의 내용을 복습하며 클론 코딩 (하지만 mypy를 사용하며 type hint 사용)
3. test code를 작성하자! (happy path라도 상관없다. 작성하는거에 의의를 두자!)
4. vanilla javascript만을 이용 (no jquery)


### 장고 mypy 사용 방법
1. 
```shell
$ mypy run django-stubs 
```
2. pyproject.toml
```toml
# mypy 에게 django plugin 을 사용
# strict = true 이어야지만 argument 와 return 값에 
# type hint 가 제대로 설정이 되어있는지 확인한다.
[tool.mypy]
plugins = ["mypy_django_plugin.main"]
python_version = 3.11
strict = true

# [[]] 의 형식을 사용하면 overrides 를 할 수 있다.
# ignore_errors = true 는 mypy 검사를 하지 않는 것
# *.migrations.* 는 개발자가 수정한 것이 아니기때문에 
# mypy 검사를 할 이유가 없다.
[[tool.mypy.overrides]]
module = "*.migrations.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = "manage"
ignore_errors = true

[tool.django-stubs]
django_settings_module = "nolzapan.settings"
```
3. run
```shell
poetry run mypy
```