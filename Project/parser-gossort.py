import requests
from bs4 import BeautifulSoup
import os


url = "https://gossortrf.ru/public/events/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

for img in soup.findAll('img'):
  print(img['src'])
  response = requests.get(f"https://gossortrf.ru{img['src']}")
  image_folder = 'image'
  image_path = os.path.join('Project', image_folder)
  os.makedirs(image_path, exist_ok=True)

  with open(os.path.join(image_path, os.path.basename(img['src'])), 'wb') as f:
    f.write(response.content)


