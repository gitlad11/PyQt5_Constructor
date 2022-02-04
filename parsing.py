from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup




def parsing():
    url = 'https://pavlodarobl.satu.kz/Videokarty'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    items = []
    names = soup.find_all('span', class_='uvIdx tg78x WZVc3 GI6Pu' )
    prices = soup.find_all('span', class_='uvIdx ILXzm')
    
    limit = 0

    try:
        for index, item in enumerate(names):
            if limit < 10:
                limit + 1
                item = { item.text : prices[index].text + 'тг.' }
                items.append(item)

    except IndexError:
        pass
    items_string = str(items)
    print(items_string)
    return items_string
