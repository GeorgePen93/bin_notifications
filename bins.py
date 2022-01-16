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

for itm in x:
    remove_newline = itm.find_all("p")[1].text.replace('\r\n', '')
    outputobject[itm.h3.text] = datetime.strptime(remove_newline, '%A, %d %B %Y').date()

print(json.dumps(outputobject, default=str, indent=4))

requests.post('https://api.telegram.org/'+config.api_key+'/sendMessage?chat_id=-761509812&text=' + json.dumps(outputobject, default=str, indent=4))