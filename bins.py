import json
import requests
import config
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://myaccount.stockport.gov.uk/bin-collections/show/100011454981"
page = urlopen(url)
html_text = page.read().decode("utf-8")
soup = BeautifulSoup(html_text,"html.parser")

x = soup.find_all("div" , {"class":"service-item"} )

outputobject = {}
i=0

for itm in x:
    remove_newline = itm.find_all("p")[1].text.replace('\r\n', '')
    date_check = datetime.strptime(remove_newline, '%A, %d %B %Y').date()
    if date_check == datetime.today().date() :
        outputobject[itm.h3.text] = date_check
        i += 1
if i > 0:
    requests.post('https://api.telegram.org/'+config.api_key+'/sendMessage?chat_id=-761509812&text=' + json.dumps(outputobject, default=str, indent=4))