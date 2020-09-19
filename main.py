import eel
import requests
from bs4 import BeautifulSoup
eel.init("web", allowed_extensions=['.js', '.html'])
@eel.expose
def scrape():
    link = eel.giveLink()()
    response = requests.get(eel.giveLink()()) 
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = None
    if 'wuxiaworld.site' in link:
        posts = soup.find(class_='breadcrumb').findAll('li')[1].get_text()
    else:   
        posts = soup.find(class_='truyen-title').get_text()
    return posts
@eel.expose
def scrape2():
    link = eel.giveLink()()
    response = requests.get(link) 
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = None
    if 'wuxiaworld.site' in link:
        posts = soup.find(class_='text-left').findAll('p')
    else:
        posts = soup.findAll('p')
    post = ''
    for p in posts:
        post += (str(p))
    post = post.replace("'","\\'")
    post = post.replace('"', '\\"')
    return post

@eel.expose
def scrapePrevious():
    link = eel.giveLink()()
    response = requests.get(link) 
    soup = BeautifulSoup(response.text, 'html.parser')
    button = None
    if 'wuxiaworld.site' in link:
        button = soup.find(class_='btn next_page')
    else:
        button = soup.findAll(class_="btn btn-success")[0]
    return button.get('href')

@eel.expose
def scrapeNext():
    link = eel.giveLink()()
    response = requests.get(link) 
    soup = BeautifulSoup(response.text, 'html.parser')
    button = None
    if 'wuxiaworld.site' in link:
        button = soup.find(class_='btn prev_page')
    else:
        button = soup.findAll(class_="btn btn-success")[1]
    return button.get('href')

eel.start("index.html", block=False)

while True:
    eel.sleep(10)