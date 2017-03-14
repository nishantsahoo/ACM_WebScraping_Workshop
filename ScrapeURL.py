import urllib3
import sys
from bs4 import BeautifulSoup
sys.stdout = open('ScrapeURL.txt', 'w')
url = "www.kashishgrover.com"
r = urllib3.PoolManager().request('GET', url).data  # http://urllib3.readthedocs.io/en/latest/user-guide.html#response-content
soup = BeautifulSoup(r, "html.parser")  # Beautiful soup object
print soup
# urllib3.PoolManager().request('GET', url).data => Returns an HTTPResponse object whose data is stored in a variable
title = soup.find('title')
# print title.text
