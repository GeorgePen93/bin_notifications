import json
import requests
import config
from urllib.request import urlopen

from datetime import datetime
y = datetime.today().date()
t=y.strftime('%Y-%m-%d')

print(t)
if '2022-02-11' == t :
    print(1)
