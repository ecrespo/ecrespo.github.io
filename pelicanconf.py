#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ernesto Crespo'
SITENAME = 'Blog de Seraph'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = 'es'
THEME = "notebook"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

SOCIAL = (('twitter', 'https://twitter.com/_seraph1'),
        ('medium', 'https://medium.com/@_seraph1'),
        ('linkedin','http://ve.linkedin.com/in/ernestocrespo'),
        ('gitlab','https://gitlab.com/ecrespo'),
        ('google+','https://plus.google.com/u/0/+ErnestoCrespo'),
        ('github', 'https://github.com/ecrespo'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
