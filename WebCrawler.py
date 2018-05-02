import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import csv

def coupe_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.cars-data.com/en/coupe-cars/page' + str(page) + '.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('a', {'class':'col-4'}):
            href = link.get('href')
            title = link.get('title')
            print(href)
            print(title)
            page += 1

def coupe_spider_links():
    html_page = urllib.request.urlopen('http://www.cars-data.com/en/coupe-cars/page2.html')
    soup = BeautifulSoup(html_page)
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
        print(links)

def coupe_text_grabber():
        html_page = urllib.request.urlopen('http://www.cars-data.com/en/coupe-cars/page2.html')
        soup = BeautifulSoup(html_page)
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^http://www.cars-data.com/pictures/")}):
            links.append(link.get('href'))
            print(links)

def coupe_spider_titles_audi():
    html_page = urllib.request.urlopen('http://www.cars-data.com/en/coupe-cars/page2.html')
    soup = BeautifulSoup(html_page, "lxml")
    titles = []
    for link in soup.findAll('a', attrs={'title': re.compile("Audi")}):
        titles.append(link.get('title'))
    print(titles)

coupe_spider_titles_audi()

def coupe_spider_titles_bmw():
    html_page = urllib.request.urlopen('http://www.cars-data.com/en/coupe-cars/page2.html')
    soup = BeautifulSoup(html_page, "lxml")
    titles = []
    for link in soup.findAll('a', attrs={'title': re.compile("BMW")}):
        titles.append(link.get('title'))
    print(titles)

coupe_spider_titles_bmw()

def coupe_spider_titles_porsche():
    html_page = urllib.request.urlopen('http://www.cars-data.com/en/coupe-cars/page2.html')
    soup = BeautifulSoup(html_page, "lxml")
    titles = []
    for link in soup.findAll('a', attrs={'title': re.compile("Porsche")}):
        titles.append(link.get('title'))
    print(titles)

coupe_spider_titles_porsche()



def write_csv():
    with open(file_path, 'a') as outcsv:
        writer = csv.writer(outcsv, delimiter = ',',  quotechar='|', quoting= csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['number', 'text', 'number'])
        for item in list:
            #Write item to outcsv
            writer.writerow([item[0], item[1], item[2]])
