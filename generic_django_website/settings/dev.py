#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Django settings for dev. """

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dxaz-4v43%9c%_&pwfbjedp$d+@zyex&gdib4s)(3-@w6@bg+8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
