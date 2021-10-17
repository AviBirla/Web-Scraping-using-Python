import requests
from bs4 import BeautifulSoup
import smtplib
import csv
import datetime 
import time
import os


url='https://www.amazon.in/Samsung-Galaxy-Snapdragon-Mystic-Storage/dp/B08GYTNRGF/ref=sr_1_3?crid=7JGF5BHIOAAX&dchild=1&keywords=samsung+note+20+ultra&qid=1634278809&sr=8-3'
header = {'User-Agaen' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


def check_price():
    page = requests.get(url , headers = header ) 
    soup = BeautifulSoup(page.content , 'html.parser')
    #print(soup.prettify())     # if u get unicode error keep this syntax as : print(soup.prettify().encode('utf-8'))
    
    product_name = soup.find('span' , class_ = 'a-size-large product-title-word-break').text
    #print(product_name)
    price = soup.find('span' , class_ = 'a-size-medium a-color-price priceBlockBuyingPriceString').text
    price=price[1:7].replace(',','')
    price=float(price)
    
    file_exixts = True
    if not os.path.exists(('./Amazon Price.csv')):
        file_exixts = False
        
    with open('Amazon Price.csv','a') as file:
        writer = csv.writer(file , lineterminator='\n')
        fields = ['TimeStamp' , 'Price(INR)']
        if not file_exixts:
            writer.writerow(fields)
            
        timestamp = f'{datetime.datetime.date(datetime.datetime.now())}'
        writer.writerow([timestamp , price])
        print('Wrote data to file .')
    
    
    return price


def send_email():
    servver = smtp.SMTP('smtp.gmail.com' , 587)   # 587 ----> port no.
    server.ehlo()                                 # establishes connection b/w ur server and google's server.
    server.starttls()
    server.ehlo()
    
    server.login('avi.birlafeb@gmail.com' , 'password')
    
    subject = f'Hey!*******ALERT !!******* the price of {product_name} has gone down.'
    body    = 'Go order now before the price fluctuates !! \n link : https://www.amazon.in/Samsung-Galaxy-Snapdragon-Mystic-Storage/dp/B08GYTNRGF/ref=sr_1_3?crid=7JGF5BHIOAAX&dchild=1&keywords=samsung+note+20+ultra&qid=1634278809&sr=8-3 '
    msg     = f'Subject : {subject} \n\n\n{body}'
    server.sendmail('avi.birlafeb@gmail.com','avi.birlafeb@gmail.com',msg)
    print('Email sent.')
    server.quit()
    
while True :
    
    price1 = check_price()
    if (price1 < 96000):
        send_email()
        break
    time.sleep(15)           
    


