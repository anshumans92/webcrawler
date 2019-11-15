from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, homepage_url, page_url):
        super().__init__()
        self.homepage_url = homepage_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print(tag)
        if tag == 'a':
            for (ats, value) in attrs:
                if ats == 'href':
                    url = parse.urljoin(self.homepage_url, value)
                    self.links.add(url)

    def get_links(self):
        return self.links


