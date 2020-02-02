import requests
from bs4 import BeautifulSoup

# paste the url
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
