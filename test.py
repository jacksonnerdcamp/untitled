from bs4 import BeautifulSoup
import requests

testsource = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(testsource, 'lxml')
print(soup.prettify())