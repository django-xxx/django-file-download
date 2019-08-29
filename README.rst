====================
django-file-download
====================

Django File Download

Installation
============

::

    pip install django-file-download


Urls.py
=======

::

    urlpatterns = [
        url(r'^f/', include('django_file_download.urls', namespace='django_file_download')),
    ]


or::

    from django.conf.urls import include, url
    from django_file_download import views as file_views

    urlpatterns = [
        url(r'^download$', file_views.file_download, name='file_download'),
    ]


Settings.py
===========

::

    INSTALLED_APPS = (
        ...
        'django_file_download',
        ...
    )

