from urllib.request import urlopen
html = urlopen("http://www.imdb.com/news/top")
print(html.read())
