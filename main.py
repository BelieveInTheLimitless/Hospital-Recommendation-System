import requests
from bs4 import BeautifulSoup

url = "https://www.swiggy.com"
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content, 'html.parser')

