import os

# create a new folder 
def create_directory(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# Create crawled and queue files
def create_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawl.txt'
    if not os.path.isfile(queue):
        text_file(queue, base_url)
    if not os.path.isfile(crawled):
        text_file(crawled, '')


# create text file
def text_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# adding and deleting file content
def append(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete(path):
    with open(path, 'w'):
        pass # do nothing


def create_set(filename):
    res = set()
    with open(filename, 'rt') as f:
        for line in f:
            res.add(line.replace('\n', ''))
    return res


# convert set to file
def convert_set(links, file):
    delete(file)
    for link in sorted(links):
        append(file, link)







