import urllib3
import sys
from bs4 import BeautifulSoup
sys.stdout = open('ScrapeURL.txt', 'w')
url = "www.kashishgrover.com"
r = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(r, "html.parser")
print soup
