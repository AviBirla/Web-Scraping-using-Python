from bs4 import BeautifulSoup
import requests
import pandas as pd

#url = 'https://sofifa.com/players?offset=0'
resultlist=[]

def get_soup(url):
    
    header = {'User_Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    
    page = requests.get(url , headers = header)
    soup = BeautifulSoup(page.content , 'html.parser')
    return soup
    #print(soup)
    
    
def get_result(soup):
    content = soup.find('tbody',{'class':'list'})
    #print(len(content))
    #print(content)
    
    for i in content :
        result = {
        'names' : i.find('div' ,{'class':'bp3-text-overflow-ellipsis'}).text ,
        'ages' :i.find('td',{'class':'col col-ae'}).text, 
        'rating' : i.find('td',{'class':'col col-oa'}).find('span').text,
        'potential' : i.find('td',{'class':'col col-pt'}).find('span').text,
        'team_name' : i.find('td',{'class':'col-name'}).find('a')['href'],
        'value' : i.find('td' , {'class':'col col-vl'}).text,
        }
        resultlist.append(result)
        
        
for x in range(0,541,60):
    soup = get_soup(f'https://sofifa.com/players?offset={x}')
    print(f'Getting page: {x}')
    get_result(soup)
    print('Total length : '+ str(len(resultlist)))   

df = pd.DataFrame(resultlist) 
df.to_excel('Fifa.xlsx' , index = False) 
print('Finished.')      