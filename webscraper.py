#requests is an HTTP library for python.This module helps to send HTTP request.
import requests

#BeautifulSoup is a Python library for pulling data out of HTMl and XML files.
from bs4 import BeautifulSoup

#Response object will be returned. Response object contains server's response to an HTTP request
response = requests.get('https://www.century21.com/real-estate/round-rock-tx/LCTXROUNDROCK/?')
#content of the response
c = response.content
#pull data from html file
soup = BeautifulSoup(c,'html.parser')

l = []
properties = soup.find_all('div',{'class':'property-card-primary-info'})
for property in properties:
    d = {}
    try:
        d['Price'] = property.find('a',{'class':'listing-price'}).text.replace('\n','').replace(' ','')
    except:
        d['Price'] = 'None'

    try:
        d['Beds'] = property.find('div',{'class':'property-beds'}).text.replace('\n','')
    except:
        d['Beds'] = 'None'

    try:
        d['Half-baths'] = property.find('div',{'class':'property-half-baths'}).text.replace('\n','')
    except:
        d['Half-baths'] = 'None'
                
    try:
        d['Sqft'] = property.find('div',{'class':'property-sqft'}).text.replace('\n','')
    except:
        d['Sqft'] = 'None'
                
    try:
        d['Address'] = property.find('div',{'class':'property-address'}).text.replace('   ','').replace('\n','')
    except:
        d['Address'] = 'None'
                
    try:
        d['City'] = property.find('div',{'class':'property-city'}).text.replace('   ','').replace('\n','')
    except:
        d['City'] = 'None'
                
    l.append(d)

print(l)


