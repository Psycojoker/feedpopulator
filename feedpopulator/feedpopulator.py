# -*- coding:Utf-8 -*-

import sys
from os import makedirs
from os.path import exists

from config import config
from handlers import FeedExtenderHandler

def check_config_dir():
    if not exists(config.path + "result"):
        makedirs(config.path + "result")

def get_feeds():
    def spliter(string):
        r = string.split(" ")
        return r[0], r[1] if len(r) > 1 else None, r[2] if len(r) > 2 else None
    return map(spliter, filter(None, open(config.path + "urls", "r").read().split("\n")))

def get_feed_handler(feed, tipe, args):
    match = {
        "extender": FeedExtenderHandler,
    }
    if tipe not in match.keys():
        return None
    return match[tipe](feed, *args.split(":"))

def run():
    check_config_dir()
    if not exists(config.path + "urls"):
        print >>sys.stderr, "Error: you don't have any ~/.config/feedpopulator/urls"

    for feed, tipe, args in get_feeds():
        handler = get_feed_handler(feed, tipe, args)
        if handler is None:
            print >>sys.stderr, "Error: no known handler for %s" % feed
            continue
        handler.generate_feed()
