from bs4 import BeautifulSoup
import requests

url = "https://commons.wikimedia.org/w/index.php?search=En-us&title=Special:MediaSearch&go=Go&type=audio&filemime=ogg"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links= soup.find_all('h3', attrs={'class':'sdms-audio-result__title'})

for link in links:
    ogg_url = link.a.get('href')
    file_name  =link.a.contents[0].strip()
    print (file_name)

    req = requests.get(ogg_url)
    url_content = req.content
    ogg_file = open(file_name, 'wb')
    ogg_file.write(url_content)
    ogg_file.close()

