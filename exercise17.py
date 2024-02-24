import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'lxml')

title = soup.find_all(class_="indicate-hover")

titles = []

for t in title:
    titles.append((t.string))
    
print(titles)