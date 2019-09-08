import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL='https://www.amazon.in/Canon-EF50MM-Lens-DSLR-Cameras/dp/B00XKSBMQA/ref=sr_1_2?crid=3076FO0ITV1LS&keywords=50mm+canon+lens&qid=1567966214&s=gateway&sprefix=50mm%2Caps%2C1279&sr=8-2'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
    
    page=requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content, 'html.parser')
             
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[0:5])

    if(converted_price>7.700):
        send_mail1()
        
    print(converted_price)
    print(title.strip())
    
    if(converted_price>7.700):
        send_mail1()
   
    
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('adish.khot@gmail.com', 'dbsprooylspjrrbm')
    
    subject='Price fell down!'
    body='Check the amazon link https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=lp_16225007011_1_4?s=computers-intl-ship&ie=UTF8&qid=1567958567&sr=1-4'
    
    msg=f"Subject:{subject}\n\n{body}"
    
    server.sendmail('adish.khot@gmail.com',
                    'adish.backups@gmail.com',
                    msg
                    )
    print('hey email has been sent')
    server.quit()
    
while(True):
    check_price()
    time.sleep(60)
    
    
    
    

