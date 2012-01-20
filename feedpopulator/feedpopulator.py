# -*- coding:Utf-8 -*-

import sys
from os import makedirs
from os.path import exists

from config import config

def check_config_dir():
    if not exists(config.path):
        makedirs(config.path)

def run():
    check_config_dir()
    if not exists(config.path + "urls"):
        print >>sys.stderr, "Error: you don't have any ~/.config/feedpopulator/urls"
