import requests
from bs4 import BeautifulSoup
import pandas as pd


#url = 'https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/product-reviews/B07BS4TJ43/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
reviewlist=[]
def get_soup(url):
    
    #r = requests.get('http://localhost8050/render.html' , params={'url':url ,'wait' : 2})
    #print(r.text)
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    page = requests.get(url , headers = header ) 
    soup = BeautifulSoup(page.content , 'html.parser')
    #print(soup.title.text)  -----> Amazon.in:Customer reviews: Canon EOS 1500D 24.1 Digital SLR Camera (Black) with EF S18-55 is II Lens
    return soup


def get_reviews(soup):
    
    reviews = soup.find_all('div', {'data-hook' : 'review'})    #find_all() will give us a list.
    try:
        for item in reviews :
            review={
            'product_name' : soup.title.text.replace('Amazon.in:Customer reviews:','').strip(),
            'title_reviews' : item.find('a',{'data-hook':'review-title'}).text.strip(),
            'rating' : float(item.find('i', {'data-hook':'review-star-rating'}).text.replace('out of 5 stars','').strip()),
            'review_body' : item.find('span',{'data-hook':'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass


for x in range(1,11):
    soup = get_soup(f'https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/product-reviews/B07BS4TJ43/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
    
df = pd.DataFrame(reviewlist) 
df.to_excel('Canon EOS 1500D Reviews.xlsx' , index = False) 
print('Finished')  