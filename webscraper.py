#requests is an HTTP library for python.This module helps to send HTTP request.
import requests

#BeautifulSoup is a Python library for pulling data out of HTMl and XML files.
from bs4 import BeautifulSoup

response = requests.get('https://www.century21.com/real-estate/round-rock-tx/LCTXROUNDROCK/?')
#content of the response
c = response.content
#pull data from html file
soup = BeautifulSoup(c,'html.parser')
print(soup)
