#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '我'
SITENAME = '我不會Java'
SITEURL = ''
THEME='./custom_theme/pelican-alchemy/alchemy'
PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISQUS_SITENAME = u"ksc91u"

# Blogroll
LINKS = (('通通寫成一行', 'https://ingramchen.io'),
         ('隨便聊天', 'https://kaif.io/'),
	('用Pelican架個人Blog','http://blog.runsheng.xyz/shi-yong-pelicanda-jian-ji-yu-gitde-jing-tai-bo-ke.html'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
