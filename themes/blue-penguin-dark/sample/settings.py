#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Tyler Carr'
SITENAME = 'Blue Penguin Dark'
SITEURL = 'http://localhost:8000'
SITELOGO = 'https://www.gravatar.com/avatar/de3ba847c89c8cab9dd7080abebf9df1'
DEFAULT_METADATE = {
    'status': 'draft',
    }


PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'


MENUITEMS = ( 
    ('GitHub', 'https://github.com/ywyz'),
    ('About', '/about.html'),
    )
# HTML metadata
SITEDESCRIPTION = ''

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# example pagination pattern
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

DARK_LIGHT_SWITCHING_OFF = False
