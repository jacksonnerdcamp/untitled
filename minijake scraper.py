from bs4 import BeautifulSoup
import requests
import re

source = requests.get('https://www.minijake.com/Furniture/').text
soup = BeautifulSoup(source,'lxml')

furniture = soup.find_all('ul')
list = []
for ul in soup.find_all('ul', class_='nscMenuContainerLevel-2 level_2'):
    try:
        list.append([ul.li.span.text, ul.li.a.get('href')])
    except Exception as e:
        pass

for i in list:
    print(i)
    print()

list2 = []
for i in list:
    page = requests.get(i[1]).text
    page_soup = BeautifulSoup(page, 'lxml')
    
    for div in soup.find_all('div', class_='caption'):
        try:
            list2.append([div.a.text, div.p.span.text])
        except Exception as e:
            pass
for i in list2:
    print(i)