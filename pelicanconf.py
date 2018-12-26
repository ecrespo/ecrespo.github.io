#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ernesto Crespo'
SITENAME = "Página de Seraph"
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Science'
SITEDESCRIPTION = ' Software Libre, Ciencia de Datos y Python'
PATH = 'content'
BROWSER_COLOR = '#333333'


TIMEZONE = 'America/Caracas'

DEFAULT_LANG = 'es'

MAIN_MENU = True

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

SOCIAL = (('linkedin', 'http://ve.linkedin.com/in/ernestocrespo'),
          ('github', 'https://github.com/ecrespo'),
          ('google', 'https://google.com/+ErnestoCrespo'),
          ('twitter', 'https://twitter.com/_seraph1'),
          ('facebook', 'https://www.facebook.com/ernesto.crespo'),
          ('gitlab', 'https://gitlab.com/ecrespo'),
          ('soundcloud','https://soundcloud.com/ernesto-crespo'),
          ('rss', '//www.seraph.to/feeds/all.atom.xml'))


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)



DISPLAY_PAGES_ON_MENU = True



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME='/home/ernesto/proyectos/ecrespo.github.io/themes/Flex'
PYGMENTS_STYLE = 'monokai'


