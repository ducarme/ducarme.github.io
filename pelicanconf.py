AUTHOR = 'Paul Ducarme'
SITENAME = 'Paul Ducarme'

PATH = "content"

THEME = './themes/pelican-tufte/pelican-tufte-theme'

SITESUBTITLE = 'Researcher in applied physics, interested in nonlinear mechanics'


TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'EN'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tufte_liquid_tags']

LIQUID_TAGS = ["img", "literal", "youtube", "audio", "include_code"]
YOUTUBE_THUMB_ONLY = True
YOUTUBE_THUMB_SIZE = 'mq'
CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
    ('AMOLF', 'https://amolf.nl/'),
    ('ARCNL', 'https://arcnl.nl/'),
    ('Soft robotic matter', 'https://overvelde.com/'),
    ('Springable', 'https://ducarme.github.io/springable/'),
)

# Social widget
SOCIAL = (
    ('Google Scholar', 'https://scholar.google.com/citations?user=rrctz-oAAAAJ'),
    ('ORCID', 'https://orcid.org/0009-0002-7429-2803'),
    ('Bluesky', 'https://bsky.app/profile/paulducarme.bsky.social'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

INDEX_SAVE_AS = 'blog.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Research', '/'),
    ('Publications', '/category/publications.html'),
    #('Teaching', '/category/teaching.html'),
    ('Talks', '/category/talks.html'),
    #('Projects', '/category/projects.html'),
    #('Blog', '/blog.html'),
    ('Photos', '/pages/photos.html'),
    ('Bio', '/pages/bio.html'),
    ('Contact', '/pages/contact.html'),
)
