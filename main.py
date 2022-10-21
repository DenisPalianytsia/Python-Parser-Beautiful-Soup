import requests
from bs4 import BeautifulSoup


for i in range(7):#Starts a cycle that will go through all the pages of the site
    url = f'https://scrapingclub.com/exercise/list_basic/?page={i + 1}'#Goes through the links of the site pages from which the information will be received
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")#Site response

    urls = soup.find_all('h4', class_='card-title')#Searches for headlines
    for i in range(len(urls)):#A cycle is started that finds links to dresses and information about them and then displays them
        urls[i] = urls[i].find('a', href=True)#Takes links of dresses
        urls[i] = urls[i]['href']
        url = f'https://scrapingclub.com/{urls[i]}'#The links of dresses
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")#Site response
        info = soup.find('div', class_='card-body').text#Searches for the necessary information and enters it into a variable
        print(info)