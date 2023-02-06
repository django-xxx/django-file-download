# django-file-download
Django File Download

## Installation
```shell
pip install django-file-download
```

## Urls.py
```python
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^f/', include('django_file_download.urls', namespace='django_file_download')),
]
```
or
```python
from django.urls import re_path
from django_file_download import views as file_views

urlpatterns = [
    re_path(r'^download$', file_views.file_download, name='file_download'),
]
```

## Settings.py
```python
INSTALLED_APPS = (
    ...
    'django_file_download',
    ...
)
```
