# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.3'


setup(
    name='django-file-download',
    version=version,
    keywords='Django File Download',
    description='Django File Download',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/django-xxx/django-file-download',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_file_download'],
    py_modules=[],
    install_requires=['TimeConvert', 'django_logit>=1.1.2', 'django-response', 'django-six', 'requests'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
