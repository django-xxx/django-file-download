# -*- coding: utf-8 -*-

from django_six import re_path

from django_file_download import views as file_views


app_name = 'django_file_download'


urlpatterns = [
    re_path(r'^download$', file_views.file_download, name='file_download'),
]
