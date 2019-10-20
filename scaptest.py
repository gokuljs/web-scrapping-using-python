from urllib.request import urlopen # imorting the library from the url request
from bs4 import BeautifulSoup
# urllib is a package that collects several modules for working with urls
# now urlopen is used open a remote object and read it


html=urlopen('http://www.pythonscraping.com/pages/page1.html')
bs=BeautifulSoup(html.read(), 'lxml')
print(bs.h1)
print(bs.body)
print(bs.body.h1)
print(bs.h2)