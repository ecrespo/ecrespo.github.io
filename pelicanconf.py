#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ernesto Crespo'
SITENAME = "Página de Seraph"
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Scientist '
EMAIL = 'ecrespo@gmail.com'
SITEDESCRIPTION = ' Software Libre, Ciencia de Datos y Python'
SITELOGO = '//s.gravatar.com/avatar/7fab2070e149e57fe99da94d7ccbad6b?s=120'
PATH = 'content'
# BROWSER_COLOR = '#333333'
BROWSER_COLOR = '#e5e5ff'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = 'es'
I18N_TEMPLATES_LANG = 'es'
DEFAULT_LANG = 'es'
OG_LOCALE = 'es_VE'
LOCALE = ("es_VE", "es_VE.utf8")

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

MARKUP = ('md', 'ipynb')


COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
    # PHP files are rendered the usual way (i.e. with the full templates).
    # The resulting files have .php extensions, making it possible to run
    # them without reconfiguring your server to recognize them.
    # "php": ('.php',),
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ('.rst', '.md', '.txt'),
}

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

SOCIAL = (('medium', 'https://medium.com/@_seraph1'),
          ('linkedin', 'http://ve.linkedin.com/in/ernestocrespo'),
          ('github', 'https://github.com/ecrespo'),
          ('google', 'https://google.com/+ErnestoCrespo'),
          ('twitter', 'https://twitter.com/_seraph1'),
          ('facebook', 'https://www.facebook.com/ernesto.crespo'),
          ('gitlab', 'https://gitlab.com/ecrespo'),
          ('soundcloud', 'https://soundcloud.com/ernesto-crespo'),
          ('rss', '//www.seraph.to/feeds/all.atom.xml'))


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


DISPLAY_PAGES_ON_MENU = True


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME = '/home/ernesto/proyectos/pelican-themes/Flex'
#THEME = '/home/ernesto/proyectos/pelican-themes/bold'
PYGMENTS_STYLE = 'monokai'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

GOOGLE_ANALYTICS = 'UA-131517246-1'
#DISQUS_SITENAME = 'seraphto'
DISQUS_SITENAME = "https://seraphto.disqus.com"
#DISQUS_SECRET_KEY= u"XoJR8Iy6JjOCBK1aBdjyPZ49pRVByB1laHszIDtb3gVU7dajxDAhevzkSZQQxrUj"
#DISQUS_PUBLIC_KEY= u""
PLUGIN_PATHS = ['./plugins', '/home/ernesto/proyectos/pelican-plugins']
PLUGINS = ['i18n_subsites',
           'better_codeblock_line_numbering',
           # 'sitemap',
           'related_posts',
           'tag_cloud',
           # 'pelican_youtube',
           'share_post',
           'neighbors',
           # 'pelican-ert',
           #           'github_activity',
           # 'pelican-ipynb.markup',
           # 'disqus_static',
           # 'pelican-gist',
           # 'pelican-githubprojects',
           # 'ipynb.markup',
           # 'pelican-toc',
           # 'ipynb.liquid',
           'post_stats']  # You may have more plugins
IGNORE_FILES = [".ipynb_checkpoints"]
# Show my last activity on GitHub
# GITHUB_USER = 'ecrespo@gmail.com'
COPYRIGHT_YEAR = 2022
# GITHUB_ACTIVITY_FEED = 'https://github.com/ecrespo.atom'
# GITHUB_ACTIVITY_MAX_ENTRIES = 10
# GITHUB_USER_TYPE = "owner"
# GITHUB_SORT_BY = "created"
# GITHUB_DIRECTION = "desc"

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/contact/">Contact</a>',
]

OUTPUT_PATH = 'docs/'


GOOGLE_FONTS = [
    'Nunito Sans:300,700',
    'Source Code Pro',
]
# https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

ERT_WPM = 200
ERT_FORMAT = '{time} read'

TOC = {
    'TOC_HEADERS': '^h[1-6]',  # What headers should be included in
    # the generated toc
    # Expected format is a regular expression

    'TOC_RUN': 'true',    # Default value for toc generation,
    # if it does not evaluate
    # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'true',     # If 'true' include title in toc
}

# MD_EXTENSIONS = [
#     'codehilite(css_class=highlight,linenums=False)',
#     'extra'
#     ]


# MARKDOWN = {
#  'extension_configs': {
#    'pyembed.markdown': {}
#  }
# }

#I18N_SUBSITES = {
#    'en': {
#        'SITENAME': 'Seraph\'s Blog',
#    }
#}

GOOGLE_ADSENSE = {
    'ca_id': 'pub-0261001661746989',    # Your AdSense ID
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'main_menu': '1234562',      # Banner before main menu (all pages)
        'index_top': '1234563',      # Banner after main menu (index only)
        'index_bottom': '1234564',   # Banner before footer (index only)
        # Banner after article title (article only)
        'article_top': '1234565',
        # Banner after article content (article only)
        'article_bottom': '1234566',
    }
}

GOOGLE_GLOBAL_SITE_TAG = 'G-300366206'
