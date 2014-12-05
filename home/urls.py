#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from home import views

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', views.index, name='index'),
)
