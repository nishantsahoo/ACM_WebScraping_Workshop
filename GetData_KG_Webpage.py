import urllib3
import sys
from bs4 import BeautifulSoup
sys.stdout = open('KG_Data.txt', 'w')
url = "www.kashishgrover.com"
r = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(r, "html.parser")
print soup.find('title')
print soup.find('title').text

