#create a webcrawler that selects a random page on wikipedia
#and then from there keeps going to the first (meaningful) link
#to finally arrive at the 'Science' wiki page
#or abandon search before if the search goes on too long
#or the search goes intp a circular loop

import requests
from bs4 import BeautifulSoup
import time
import urllib

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Science"
article_chain = []

article_chain.append(start_url)

def find_first_link(article):
    response = requests.get(article)
    html = response.text #type <string>
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    article_link = None
    
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    
    if not article_link:
        return
    else:
        first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
        return first_link

def web_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        print(search_history[-1])
        print("We've found the target article!!!")
        return False
    elif len(search_history) > 25:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print(search_history[-1])
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True

while web_crawl(article_chain,target_url):
    print(article_chain[-1])
    next_link = find_first_link(article_chain[-1])

    if not next_link:
        print("we've reached an article with no further links, aborting search!")
        break
    else:
        article_chain.append(next_link)
    
    time.sleep(2)



