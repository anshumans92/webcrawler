from urllib.parse import urlparse

def get_domain(url):
    try:
        results = get_subdomain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
    
def get_subdomain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

