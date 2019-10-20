from urllib.request import urlopen  # urlopen is used to read file format (remote)
from urllib.error import HTTPError # throughs an exception during the http error
from bs4 import BeautifulSoup
def getTitle(url):
 try:
    html = urlopen(url) # reading ht eremote file
 except HTTPError as e:  # checking the any http excption is present
    return None
 try:
    bs = BeautifulSoup(html.read(), 'html.parser')  #passed it beautiful soup
    title = bs.body.h1 # passing the firs h1 tag
 except AttributeError as e:  # excption occurs if the given attribute dosent occur
    return None
 return title  # else retutrning the title
title = getTitle('http://www.pythonscraping.com/pages/page1.html') # creating a funtion and passing get title
if title == None:
 print('Title could not be found')
else:
 print(title)
