#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Django settings for production. """

from .common import *
from .secret_key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['www.yourwebsite.com', 'yourwebsite.com',
                 'subdomain.yourwebsite.com']
