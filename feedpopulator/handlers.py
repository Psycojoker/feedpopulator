from urllib2 import urlopen
from feedparser import parse
from feedformatter import Feed
from BeautifulSoup import BeautifulSoup
from dateutil.parser import parse as date_parse
from time import mktime

from config import config

class FeedHandler():
    def generate_feed(self):
        raise NotImplemented


class FeedExtenderHandler(FeedHandler):
    def __init__(self, url, key, attr="class", tag="div"):
        self.url = url
        self.key = key
        self.attr = attr
        self.tag = tag

    def file_name(self):
        return self.url.split("/")[2]

    def generate_feed(self):
        orig = parse(self.url)
        result = Feed()
        result.feed["title"] = orig.feed.title
        result.feed["description"] = orig.feed.description
        result.feed["link"] = orig.feed.link

        for i in orig.entries:
            soup = BeautifulSoup(urlopen(i.link).read())
            content = unicode(soup.find(self.tag, **{self.attr: self.key}))
            result.items.append(dict(description=content, title=i.title, link=i.link, guid=i.get("guid"), pubDate=mktime(date_parse(i.get("date")).timetuple())))

        result.format_rss2_file(config.path + "result/" + self.file_name())
