import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/feed/trending'
response = requests.get(url)  # get request to url, record as response
soup = BeautifulSoup(response.text, "html.parser")  # create an instance of BeautifulSoup class
images = soup.find_all("img")  # gets all img tags from raw html

counter = 0
for img in images:  # go through all img tags 
    if img['src'][-3:] != 'gif':
        path = './images/' + str(counter) + '.jpg'
        with open(path, 'wb') as f:
            response = requests.get(img['src'])
            f.write(response.content)
        counter += 1


        

        