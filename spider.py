from urllib.request import urlopen
from get_links import LinkFinder
from web_crawler import *


class Spider:
    project = ''
    base_url = ''
    domain = ''
    queue_set = set()
    crawl_set = set()
    queue_file = ''
    crawl_file = ''
    
    def __init__(self, project, base_url, domain):
        Spider.project = project
        Spider.base_url = base_url
        Spider.domain = domain
        Spider.queue_file = project + '/queue.txt'
        Spider.crawl_file = project + '/crawl.txt'
        self.boot()
        self.crawl('Initial crawl', Spider.base_url)

    @staticmethod
    def boot():
        create_directory(Spider.project)
        create_files(Spider.project, Spider.base_url)
        Spider.queue_set = create_set(Spider.queue_file)
        Spider.crawl_set = create_set(Spider.crawl_file)

        
    @staticmethod
    def crawl(thread, page_url):
        if page_url not in Spider.crawl_set:
            print(thread + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue_set)) +
                  ' | Crawled ' + str(len(Spider.crawl_set)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue_set.remove(page_url)
            Spider.crawl_set.add(page_url)
            Spider.update()

    @staticmethod
    def gather_links(page_url):
        html = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url,page_url)
            finder.feed(html)
        except:
            print('Error: Can not crawl page')
            return set()
        return finder.get_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue_set:
                continue
            if url in Spider.crawl_set:
                continue
            if Spider.domain not in url:
                continue
            Spider.queue_set.add(url)

    @staticmethod
    def update():
        convert_set(Spider.queue_set, Spider.queue_file)
        convert_set(Spider.crawl_set, Spider.crawl_file)
            

        
        
