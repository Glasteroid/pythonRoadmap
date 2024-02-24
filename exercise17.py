import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'lxml')

class_names = [
    "indicate-hover",
    "css-vf1hbp",
    "css-66vf3i",
    "css-1gb49m4",
    "css-1j7a2zk",
    "css-1qmga95"
]

title = soup.find_all(class_=class_names)

titles = []

for t in title:
    titles.append(t.text)
    
print(titles)
    


