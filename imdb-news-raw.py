from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.imdb.com/news/top")
imdbNews = BeautifulSoup(html.read(), "html.parser")
print(imdbNews.h2)
