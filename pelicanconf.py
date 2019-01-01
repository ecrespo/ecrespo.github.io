#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ernesto Crespo'
SITENAME = "Página de Seraph"
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Science'
SITEDESCRIPTION = ' Software Libre, Ciencia de Datos y Python'
SITELOGO = '//s.gravatar.com/avatar/7fab2070e149e57fe99da94d7ccbad6b?s=120'
PATH = 'content'
BROWSER_COLOR = '#333333'
#BROWSER_COLOR = '#e5e5ff'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = 'es'
I18N_TEMPLATES_LANG = 'es'
DEFAULT_LANG = 'es'
#OG_LOCALE = 'es_VE'
#LOCALE = 'es_VE'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

MAIN_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

SOCIAL = (('medium', 'https://medium.com/@_seraph1'),
          ('linkedin', 'http://ve.linkedin.com/in/ernestocrespo'),
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

GOOGLE_ANALYTICS = 'UA-131517246-1'
#DISQUS_SITENAME = 'seraphto'
DISQUS_SITENAME = "https://seraphto.disqus.com"
PLUGIN_PATHS = ['plugins']
#PLUGINS = ['pelican-js'] # You may have more plugins

COPYRIGHT_YEAR = 2006

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/contact/">Contact</a>',
]

GOOGLE_FONTS = [
    'Nunito Sans:300,700',
    'Source Code Pro',
]

