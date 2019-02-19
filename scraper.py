import urllib3
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, 'html.parser')
links = soup.select("table.chart .lister-list a")
# print(links)
for link in links:
    # link = link.replace('\n', ' ').replace('\r', '')
    print(link)

# print(soup.find('title').text)
# print(soup.title.string)
# print(soup.prettify())
# soup = BeautifulSoup(ourUrl, "lxml")
# print(soup.find('title').text)
