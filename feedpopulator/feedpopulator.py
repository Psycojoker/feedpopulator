# -*- coding:Utf-8 -*-

import sys
from os import makedirs
from os.path import exists

from config import config

def check_config_dir():
    if not exists(config.path):
        makedirs(config.path)

def get_feeds():
    return filter(None, open(config.path + "urls", "r").read().split("\n"))

def get_feed_handler(feed):
    return None

def run():
    check_config_dir()
    if not exists(config.path + "urls"):
        print >>sys.stderr, "Error: you don't have any ~/.config/feedpopulator/urls"

    for feed in get_feeds():
        if get_feed_handler(feed) is None:
            print >>sys.stderr, "Error: no known handler for %s" % feed
