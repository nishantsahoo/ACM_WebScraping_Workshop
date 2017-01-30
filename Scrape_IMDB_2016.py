import urllib3
import sys
from bs4 import BeautifulSoup
from tqdm import tqdm
for year in range(2010,2017):
    sys.stdout = open('IMDB_Top_50_' + str(year) +'_urllib3.txt', 'w')
    url = "http://www.imdb.com/search/title?release_date=" + str(year) + ',' + str(year) + "&title_type=feature"
    r = urllib3.PoolManager().request('GET', url).data
    soup = BeautifulSoup(r, "html.parser")
    article = soup.find('div', attrs={'class': 'article'}).find('h1')
    print article.contents[0] + ': '
    lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
    i = 1
    movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
    for div in tqdm(movieList):
        print str(i) + '.',
        header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
        for items in header:
            title = header[0].findChildren('a')
            print 'Movie: ' + str(title[0].contents[0].encode('utf-8').decode('ascii', 'ignore'))
        i += 1