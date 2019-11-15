import threading
from queue import Queue
from spider import Spider
from domain import *
from web_crawler import *

project = 'jobsearch'
homepage = 'https://www.monster.com/jobs/search/?q=Software-Engineer&intcid=skr_navigation_nhpso_searchMain'
domain = get_domain(homepage)
queue_file = project + '/queue.txt'
craw_file = project + '/crawl.txt'
threads = 8
queue = Queue()
Spider(project, homepage, domain)

def crawl1():
    queued_links = create_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

def create_jobs():
    for link in create_set(queue_file):
        queue.put(link)
    queue.join()
    crawl1()
