AUTHOR = 'Paul Ducarme'
SITENAME = 'Paul Ducarme'

PATH = "content"

THEME = 'themes/pelican-tufte/pelican-tufte-theme'

SITESUBTITLE = 'Researcher in applied physics, interested in nonlinear mechanics'


TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

# Social widget
SOCIAL = (
    ('Scopus', '#'),
    ('ORCID', '#'),
    ('Google Scholar', '#'),
    ('Twitter', '#'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

INDEX_SAVE_AS = 'blog.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Publications', '/category/publications.html'),
    ('Teaching', '/category/teaching.html'),
    ('Talks', '/category/talks.html'),
    ('Projects', '/category/projects.html'),
    ('Blog', '/blog.html'),
    ('Contact', '/pages/contact.html'),
)
