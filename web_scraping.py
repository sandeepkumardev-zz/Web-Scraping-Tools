# module for http request
import requests
# module for access code
from bs4 import BeautifulSoup

# paste the url
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# print code
print(soup)
