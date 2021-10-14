from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url = 'https://www.amazon.in/s?k=nike+shoes+for+men&crid=AKYEB60SO7G6'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text , 'html.parser')
    return soup



def getnextpage(soup):
    page = soup.find('ul' , {'class':'a-pagination'})
    if not page.find('li' , {'class':'a-disabled a-last'}):
        url = 'http://www.amazon.in' + str(page.find('li' , {'class':'a-last'}).find('a')['href'])
        return url
    else:
        return
    
while True :
    
    soup = getdata(url)
    url = getnextpage(soup)
    if not url :
        break
    print(url)