import requests
from bs4 import BeautifulSoup as bs
import csv

def get_html(url):
    response = requests.get(url)
    # print(response)
    return response.text

def to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['img'], data['description']])

def get_description(url):
    html = get_html(url)
    soup = bs(html, 'lxml')
    description = soup.find('p', class_ ='comment').text
    return description


def get_data(html):
    soup = bs(html, 'lxml')
    cars = soup.find('div', class_ = 'table-view-list').find_all('div', class_ = 'list-item')
    # print(cars)
    for car in cars:
        title = car.find('h2', class_ = 'name').text.strip()
        price = car.find('strong').text
        price = price.replace('\n','').replace(' ', '')

        img = car.find('img').get('src')
        # print(img)

        desc_url = car.find('a').get('href')
        desc_url = 'https://www.mashina.kg'+ desc_url
        description = get_description(desc_url)


        data = {
            'title': title,
            'price': price,
            'img': img,
            'description': description
        }
        to_csv(data)


url = 'https://www.mashina.kg/search/alt/'

# print(get_html(url))
with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title','price','img','description'])

get_data(get_html(url))



# plagintion