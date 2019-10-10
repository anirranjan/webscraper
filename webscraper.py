import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/feed/trending'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
images = soup.find_all("img")

save_counter = 0
for img in images:
    if img['src'][-3:] != "gif":
        path = './images/img_' + str(save_counter) + '.jpg'
        with open(path, 'wb') as f:
            response = requests.get(img['src'])
            f.write(response.content)
        save_counter += 1
        
        
