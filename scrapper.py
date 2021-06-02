import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Enter the stockX link you want
URL = 'https://stockx.com/adidas-yeezy-boost-350-v2-core-black-red-2017'

headers = {
    "User-agent": 'User-agent'}
    #Edit the header above by adding your own User_agent by googling "My user Agent"

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    title = soup.find(id='product-header').get_text()
    # print(title.strip())

    price = soup.find(id='market-summary').get_text()
    # print(price.strip())

    Average_price = float(price[32:35])
    # print(Average_price)

    #Edit this Condition to what you want
    if(Average_price < 400):
        send_email()


def send_email():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #change this to your email
    server.login('email@gmail.com', 'password')

    subject = 'Price fell down'
    
    #Change the link to the link you also provide above to get the link to the StockX page
    body = 'Check the StockX link https://stockx.com/adidas-yeezy-boost-350-v2-core-black-red-2017'

    msg = f"Subject: { subject}\n\n{body}"

    server.sendmail(
        #change this email to the email you want to use as the sender
        'email@gmail.com',
        
        #change this email to the email you want to use as the reciever
        'email@gmail.com',
        msg
    )
    print('Email was sent')

    server.quit()


while(True):
    check_price()
    time.sleep(3600)  # Checks once every hour by seconds, you can also change this
