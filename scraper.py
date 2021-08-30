import requests
from bs4 import BeautifulSoup
import smtplib
import time




def check_price():
    url = 'https://www.amazon.in/ASUS-Dash-F15-15-6-inch-i5-11300H-FX516PC-HN057T/dp/B096KWK1DB/ref=dp_prsubs_1?pd_rd_i=B096KWK1DB&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

    currentPrice=0
    page=requests.get(url,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title= soup.find('span',{'id':'productTitle'}).get_text()
    price= soup.find('span',{'id': 'priceblock_ourprice'}).get_text()

    converted_price=int((price[1:7]).replace(',',''))

    previous_price=get_var_value()

    if converted_price>previous_price:
        send_mail()
        update_price(converted_price)


def get_var_value(filename="price.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0)
        return val

def update_price(new_price):
    with open("price.dat", "w") as f:
        f.write(str(new_price))
    print("Value Updated",new_price)


def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('amartya0009@gmail.com','xuxgufqnczpmidtj')

    subject='Alert! Price reduced'
    body='Check amazon link https://www.amazon.in/ASUS-Dash-F15-15-6-inch-i5-11300H-FX516PC-HN057T/dp/B096KWK1DB/ref=dp_prsubs_1?pd_rd_i=B096KWK1DB&psc=1'
    msg =f"subject:{subject}\n\n{body}"
    server.sendmail('amartya0009@gmail.com','2020.sujan.gh@gmail.com',msg)
    print("mail Sent")
    server.quit()

while(True):
    check_price()
    time.sleep(10800)





