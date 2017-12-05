from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.imdb.com/news/top")
imdbNews = BeautifulSoup(html, "html.parser")
for headline in imdbNews.findAll("h2"):
    print(headline)
