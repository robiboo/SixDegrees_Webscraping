from bs4 import BeautifulSoup, SoupStrainer
from bs4 import SoupStrainer
from collections import deque
import requests, re, gc


#Test urls
#r = requests.get("https://en.wikipedia.org/wiki/George_Lucas")
#r = requests.get("https://en.wikipedia.org/wiki/Mellody_Hobson")
#All test wokrs

#randomly gives a page/url
def get_random_page_url():
	r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
	return r.url

#filters the page
def internal_not_special(href):
    if href:
        if re.compile('^/wiki/').search(href):
            if not re.compile('/\\w+:').search(href):
                if not re.compile('#').search(href):
                    return True
    return False

#a queue of all visited page
linksVisited = {}

#makes the path
path = deque([])

#counts the number of hops
hop = 0

def webscrapingDFS(url, hop, linksVisited, path):
    """
    A function that takes an initial link and does webscraping.
    Finding a path until it finds the wiki page of StarWars
    """

    linkstart = requests.get(url)

    #parse only things inside the 'a'
    a_only = SoupStrainer('a')
    page = BeautifulSoup(linkstart.text, 'html.parser', parse_only=a_only)

    #parse the heading only for titles
    h1_only = SoupStrainer('h1', {'id' : 'firstHeading'})
    pageTitle = BeautifulSoup(linkstart.text, 'html.parser', parse_only=h1_only)

    linkstart.close()
    href = page.find_all('a', href=internal_not_special)

    #freeing memory
    page.decompose()
    gc.collect()

    hop += 1
    
    if(pageTitle.string != None):
        print(pageTitle.string)

        path.append(pageTitle.string + " (" + linkstart.url + ")")

        #loops through the page's body and checks all links if Star Wars exist before hopping
        for link in href:
            if link.string not in linksVisited:
            
                if(link.get('href') == "/wiki/Star_Wars"): 

                    path.append("Star Wars (https://en.wikipedia.org/wiki/Star_Wars)")
                    return True;

        linksVisited[pageTitle.string] = link.get('href')

        if(hop == 6):
                    path.pop()
                    return False;

        else:
            #recursing or hopping
            for find in href:
        
                if find.string not in linksVisited:

                    #preps the new url for recursion
                    newLink = "https://en.wikipedia.org" + find.get('href')

                    if(webscrapingDFS(newLink, hop, linksVisited, path)):
                        return True

        path.pop()
        return False

webscrapingDFS(get_random_page_url(), hop, linksVisited, path)
print("\n")

#if path(deuqe) empty prints a string
if(len(path)==0):
    print("No path found")
else:
    #loops thru the deque and prints the elements in the deque or the path
    for result in range(0, len(path)):
        print(result+1, "\t" + path[result] + "\n")