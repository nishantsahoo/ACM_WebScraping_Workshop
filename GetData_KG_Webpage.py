import urllib3
import sys
from bs4 import BeautifulSoup
sys.stdout = open('KG_Data.txt', 'w')
url = "www.kashishgrover.com"
r = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(r, "html.parser")
exp = soup.find('div', attrs={'class':'flexin'})
shippable = exp.find('div', attrs={'id':'shippable'})
blurb = shippable.find('div', attrs={'class':'blurb'})
ul = blurb.find('ul')
list = ul.findAll('li')
for each in list:
    print each.text
