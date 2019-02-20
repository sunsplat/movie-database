import requests, urllib3
from lxml import html, etree
from bs4 import BeautifulSoup

# Using urllib3 with BeautifulSoup:
url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, 'html.parser')
links = soup.select("table.chart .lister-list a")

# Using requests with xpath and lxml:
url2 = "https://www.imdb.com/best-of/top-100-shows-of-2018/ls045252633/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=b01789be-dffd-4aff-a31d-6eead051021a&pf_rd_r=GR0XJ2Y6DMB1YVXBSKAA&pf_rd_s=center-7&pf_rd_t=60601&pf_rd_i=best-of&ref_=fea_bo16_pks_tv_hd"
imdb_page = requests.get(url2)
page_content = html.fromstring(imdb_page.content) # need
movie_block = page_content.xpath('//*[@data-caller-name="list-title"]/div/div/div/h3[@class="lister-item-header"]/a/text()')
for block in movie_block:
    print(block)
    # print(etree.tostring(block))


# links2 = soup.findAll('h3', attrs={'class':'image'})
# for link in links:
#     print(link)

# print(soup.find('title').text)
# print(soup.title.string)
# print(soup.prettify())
# soup = BeautifulSoup(ourUrl, "lxml")
# print(soup.find('title').text)
