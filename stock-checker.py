from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse
import requests
import sys
import time
import lxml

print('Made by @MJsneaks1')
while True:
    def getTime():
        return time.strftime('|%D | %H:%M:%S|')
    def getURL():
        print('___________________________________________________________________________________________________________________________________________________________')
        print('')
        global r
        global soup
        global URL
        print(getTime())
        print('')
        print('choose one:')
        print('1. Paste a shopify link')
        print('2. Search for a shopify product using keywords')
        choice = input('Type the number of the action you would like to take: ')
        while (choice != '11') and (choice != '22'):
            if choice == '1':
                URL = input('Paste shopify link here: ')
                if '?' in URL:
                    URL, y, z = URL.partition('?')
            elif choice == '2':
                website = input('What website do you want to cop from? Only type the website name (i.e. kith.com) ')
                keyword1 = input('Type 1 keyword to search for the product: ')
                keyword2 = input('Type another keyword to specify the product: ')
                keyword3 = input('Type another keyword to specify the product, or leave blank: ')
                keyword4 = input('Type another keyword to specify the product, or leave blank: ')
                keyword5 = input('Type another keyword to specify the product, or leave blank: ')
                keyword6 = input('Type another keyword to specify the product, or leave blank: ')
                s = requests.Session()
                f = s.get('https://'+website+'/sitemap_products_1.xml')
                soup1 = BeautifulSoup(f.text, 'lxml')
                products = soup1.find_all('url')
                for url in products:
                    if keyword1 in url.get_text():
                        URL = (url.find('loc').text)
                        if keyword2.lower() in URL:
                            if keyword3.lower() in URL:
                                if keyword4.lower() in URL:
                                    if keyword5.lower() in URL:
                                        if keyword6.lower() in URL:
                                            print('')
                                            print('Product url: {}'.format(URL))
                                            print('(!)If the incorrect url was found you probably chose shitty keywords(!)')
                                            return URL

            break
    def getSoup():
        global soup
        s = requests.Session()
        r = s.get(URL+'.xml')
        soup = BeautifulSoup(r.text, 'lxml')
        return soup
    def getItem():
        global item
        item = soup.find('title').text
    def getSize():
        global sz
        sz = list()
        for size in soup.find_all('title')[1:]:
            sz.append(size.get_text())
        return sz
    def getStock():
        global stk
        stk = list()
        for stock in soup.find_all('inventory-quantity'):
            stk.append(stock.get_text())
        return stk
    def getPrice():
        global prc
        prc = list()
        for price in soup.find_all('price'):
            prc.append(price.get_text())
        return prc
    def getVariants():
        global vrnt
        vrnt = list()
        for variants in soup.find_all('product-id'):
            vrnt.append(variants.find_previous('id').get_text())
        return vrnt
    def getTotal():
        global ttl
        ttl = list()
        for stocktotal in soup.findAll("inventory-quantity"):
            ttl.append(int(stocktotal.text))
        return ttl
    [getURL(), getSoup(), getItem(), getSize(), getStock(), getPrice(), getVariants(), getTotal()]
    def formatData():
        print('')
        print(item)
        if len(stk)>0:
            print('{:<5} | {:<20} | {:<10} | {:10} | {:20} '.format('', 'size', 'stock', 'price', 'variants'))
            for i, (size, stock, price, variant) in enumerate(zip(sz, stk, prc, vrnt)):
                print('{:<5} | {:<20} | {:<10} | {:10} | {:20} '.format(i, size, stock, '$'+price, variant))
            if sum(ttl) == 0:
                print('Sold out!')
            elif sum(ttl) != 0:
                print('Total stock: {:<5}'.format(sum(ttl)))
        else:
            print('Stock could not be found :(')
            print('{:<5} | {:<20} | {:10} | {:20} '.format('', 'size', 'price', 'variants'))
            for i, (size, price, variant) in enumerate(zip(sz, prc, vrnt)):
                print('{:<5} | {:<20} | {:10} | {:20} '.format(i, size, '$'+price, variant))
    formatData()
    def ATC():
        print('')
        choice = input('Would you like to buy this item? (y/n) ')
        while (choice != 'y1') and (choice != 'n1'):
            if choice == 'y':
                size = input('What size from the list above do you need? ')
                quantity = input('How many of this item would you like to purchase? ')
                try:
                    variant = soup.find(text=size).findPrevious('id').text
                except AttributeError:
                    print('')
                    print('(!)Size could not be found, make sure to input your size in the same format as in the list above (i.e. if the list says medium, type medium, NOT just m) it is case-sensitive(!)')
                    print('')
                    print("Let's try this again...")
                    size = input('What size from the list above do you need? ')
                    variant = soup.find(text=size).findPrevious('id').text
                url = urlparse(URL)
                baseurl = 'https://'+url.netloc+'/cart/'
                BD = baseurl+variant+':'+quantity
                driver = webdriver.Chrome()
                driver.get(BD)
                [getURL(), getSoup(), getItem(), getSize(), getStock(), getPrice(), getVariants(), getTotal(), formatData(), ATC()]
            elif choice == 'n':
                    choice1 = input('Would you like to search for another product? (y/n) ')
                    while (choice1 != 'yo') and (choice1 != 'no'):
                        if choice1 == 'y':
                            [getURL(), getSoup(), getItem(), getSize(), getStock(), getPrice(), getVariants(), getTotal(), formatData(), ATC()]
                        else:
                            print('Ok, closing shopify stock checker')
                            sys.exit()

    ATC()
