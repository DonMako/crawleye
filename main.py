import urllib
from urllib import request
from bs4 import BeautifulSoup as BS


def main():

    # On stocke les urls des pages déjà croisées, pour ne pas stocker 
    liste_urls = []

    # On initialise l'objet url, qui va nous permettre de faire la recherche
    url = "https://ensai.fr/"

    while len(liste_urls) < 50:

        url_request = urllib.request.urlopen(url)
        soup = BS(url_request, 'html.parser')
        urls_found = []
        for link in soup.find_all('a'):
            urls_found.append(link.get('href'))

        for link in urls_found:
            if link not in liste_urls and link != '#header':
                liste_urls.append(link)
    
    f = open("crawled_webpages.txt", "w")
    for link in liste_urls:
        f.write(link)
        f.write("\n")
    f.close()

main()