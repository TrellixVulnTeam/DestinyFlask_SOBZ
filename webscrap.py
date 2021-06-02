from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

df = pd.DataFrame()
html_text = requests.get('https://www.blueberries.gg/weapons/destiny-2-exotic-tier-list/').text
soup = BeautifulSoup(html_text,'lxml')
wholerow = soup.find('tbody', class_ = 'row-hover')
row = wholerow.find_all('div', class_ = 'weapon')

weaponlist = []
for x in row:
    weaponlist.append(x.text)

df.append(weaponlist)
df



