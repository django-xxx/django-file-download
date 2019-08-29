# django-file-download
Django File Download

## Installation
```shell
pip install django-file-download
```

## Urls.py
```python
urlpatterns = [
    url(r'^f/', include('django_file_download.urls', namespace='django_file_download')),
]
```
or
```python
from django.conf.urls import include, url
from django_file_download import views as file_views

urlpatterns = [
    url(r'^download$', file_views.file_download, name='file_download'),
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
