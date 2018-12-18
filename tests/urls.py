# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django
from django.conf.urls import url, include

from rest_framework_tus.urls import urlpatterns as rest_framework_tus_urls

if django.VERSION >= (2, 0):
    urlpatterns = [
        url(r'^', include((rest_framework_tus_urls, 'tests'), namespace='rest_framework_tus')),
    ]
else:
    urlpatterns = [
        url(r'^', include(rest_framework_tus_urls, namespace='rest_framework_tus')),
    ]
