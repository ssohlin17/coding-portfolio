#scrape top news articles from crypto news sites
#Sites: Decrypt.io, cointelegraph.com, coindesk.com
#should send urls with first 4 lines of news article?

#Additionally scrape specific news about coins/tokens/protocols that I seem interested in
#Interests: ALGO, XLM, ADA, ETH, MATIC, GALA, Gaming coins

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.message import EmailMessage
from email import encoders
import os

import smtplib
from email.mime.text import MIMEText
import config
from bs4 import BeautifulSoup as bs
import requests
from requests.api import head
from smtplib import SMTP

def send_email(subj, msg):
    #sending email to myself via secondary gmail account

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(config.FROM_EMAIL_ADDRESS, config.PASSWORD) 
        message = EmailMessage()
        message['Subject'] = subj
        message['From'] = config.FROM_EMAIL_ADDRESS
        message['To'] = config.TO_EMAIL_ADDRESS
        message.set_content("Top 3 from the Big 3")
        message.add_alternative(msg, subtype='html')
        server.send_message(message)
        server.quit()
        print("success - email sent!")
    except:
        print("email didn't send")


url1 = "http://www.coindesk.com"
url2 = "https://cointelegraph.com/"


headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
re1 = requests.get(url1, headers=headers)
re2 = requests.get(url2, headers=headers)

if re1.status_code == 200:
    soup = bs(re1.content, "lxml")
    div = soup.find_all('div', attrs={"class": "most-read-articlestyles__Title-sc-1j39yzb-1 qEjiD"})
    
    website = "Coin Desk"
    headlines = {"title": [], "url": []}
    for link in div:
        headlines["title"].append(link.find('a').text)
        headlines["url"].append(link.find('a')['href'])
    
    message = ""
    count = 0
    while count < len(headlines["url"]):
        message = message + "Link: <a href=\"" + str(url1) + str(headlines["url"][count]) + "\">" + str(headlines["title"][count]) + "</a><br>"
        count += 1
    
    message1 = str(website) +  "<br><br>" +  str(message)

if re2.status_code == 200:
    soup = bs(re2.content, "lxml")
    anchor = soup.find_all('a', attrs={"class": "main-news-controls__link"})
    
    website = "Coin Telegraph"
    headlines = {"title": [], "url": []}
    for link in anchor:
        headlines["title"].append(link.text.strip())
        headlines["url"].append(link.get('href'))
    
    count = 0
    while count < len(headlines["url"]):
        message = message + "Link: <a href=\"" + str(url1) + str(headlines["url"][count]) + "\">" + str(headlines["title"][count]) + "</a><br>"
        count += 1

    message2 = str(website) + "<br><br>" + str(message)

subject = "Crypto Top News"
break_lines = "<br><br>"
formatted_message = "<!DOCTYPE html><html><body>" + message1 + break_lines + message2 + break_lines + "</body></html>"
send_email(subject, formatted_message)