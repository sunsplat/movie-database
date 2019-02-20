import requests, urllib3, re
from lxml import html, etree
from bs4 import BeautifulSoup

class MovieDb():
    def __init__(self, user_choice, limit, url):
        self = self
        self.user_choice = user_choice
        self.limit = limit
        self.url = url

    def getMovieData(self):
        if self.user_choice == '1':
            # Using urllib3 with BeautifulSoup:
            all_movies = urllib3.PoolManager().request('GET', self.url).data
            soup = BeautifulSoup(all_movies, 'html.parser')
            links = soup.find_all("td", class_="titleColumn")
            return links
        else:
            imdb_page = requests.get(self.url)
            page_content = html.fromstring(imdb_page.content) # need
            movie_block = page_content.xpath('//*[@data-caller-name="list-title"]/div/div/div/h3[@class="lister-item-header"]/a/text()')
            return movie_block

    def printData(self):
        data = self.getMovieData()
        if self.user_choice == '1':
            for i in range(self.limit):
                movie_info = re.sub('\W+',' ', data[i].text)
                print(movie_info)
        else:
            for i in range(self.limit):
                print(data[i])

    # i = 0
    # if user_choice == '1':

        # url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
        # ourUrl = urllib3.PoolManager().request('GET', url).data
        # soup = BeautifulSoup(ourUrl, 'html.parser')
        # links = soup.find_all("td", class_="titleColumn")
    #     for i in range(limit):
    #         movie_info = re.sub('\W+',' ', links[i].text)
    #         print(movie_info)
    # elif user_choice == '2':
        # Using requests with xpath and lxml:
        # url2 = "https://www.imdb.com/best-of/top-100-shows-of-2018/ls045252633/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=b01789be-dffd-4aff-a31d-6eead051021a&pf_rd_r=GR0XJ2Y6DMB1YVXBSKAA&pf_rd_s=center-7&pf_rd_t=60601&pf_rd_i=best-of&ref_=fea_bo16_pks_tv_hd"
        # imdb_page = requests.get(url2)
        # # page_content = BeautifulSoup(imdb_page.content, "html.parser")
        # page_content = html.fromstring(imdb_page.content) # need
        # movie_block = page_content.xpath('//*[@data-caller-name="list-title"]/div/div/div/h3[@class="lister-item-header"]/a/text()')
    #     for i in range(limit):
    #         print(movie_block[i])
    # else:
    #     print("Not a valid choice! Choose again!")

if __name__ == "__main__":
    print("I want to see top movies:\n1. ALL \n2. 2018")
    user_choice = input("Choice (1, 2):")
    limit = int(input("Limit (0-100):"))
    if user_choice == '1':
        url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
    elif user_choice == '2':
        url = "https://www.imdb.com/best-of/top-100-shows-of-2018/ls045252633/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=b01789be-dffd-4aff-a31d-6eead051021a&pf_rd_r=GR0XJ2Y6DMB1YVXBSKAA&pf_rd_s=center-7&pf_rd_t=60601&pf_rd_i=best-of&ref_=fea_bo16_pks_tv_hd"
    else:
        print("CHOICE IS INVALID")
    movie_db = MovieDb(user_choice, limit, url)
    movie_db.printData()
