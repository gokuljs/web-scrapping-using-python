from urllib.request import urlopen  #used to open remote object and read it
from urllib.error import HTTPError  #it is used to through an exception if any library error is there
from urllib.error import URLError   #to check any url exception is there
from bs4 import BeautifulSoup

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com') ## tries to read the web page first
except HTTPError as e:  ##calls an http error
    print(e)
except URLError as e:   ## calls an url error
    print('The server could not be found!')
else:
    print('It Worked!')

