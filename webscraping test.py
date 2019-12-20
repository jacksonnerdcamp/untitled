from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text

# parsing a website using lxml
soup = BeautifulSoup(source, 'lxml')

# finding the first instance of an article
article = soup.find('article')
print(article.prettify())

# use find method when looking for a specific class
paragraph = soup.find('p', class_='site-description')
print(paragraph.text)

# finding all of the headlines using a loop
for(article) in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

# using find to locate a video link, then manipulating that link
vid_src = soup.find('iframe')['src']
vid_id = vid_src.split('/')
print(vid_id)
vid_id = vid_id[4]

"""
alternatively, use:
ul = soup.find('ul')
ul...parent structure...a.get('href')
"""

# forming a new link from the embedded link
link = f'https://youtube.com/watch?v={vid_id}'
print(link)

# saving the scraped page
import csv
csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary', 'videolink'])

# for each iteration of a for loop, write a new row of the csv file.
csv_writer.writerow([headline, paragraph, link])
csv_file.close()
