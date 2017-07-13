from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse
import requests
import sys

print('Made by @MJsneaks1')
while True:
    def getURL():
        print('')
        global URL
        global r
        global soup
        URL = input('Paste shopify link here: ')
        if '?' in URL:
            URL, y, z = URL.partition('?')
        s = requests.Session()
        r = s.get(URL+'.xml')
        soup = BeautifulSoup(r.text, 'xml')
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
    [getURL(), getItem(), getSize(), getStock(), getPrice(), getVariants(), getTotal()]
    def formatData():
        print('')
        print(item)
        if len(stk)>0:
            print('{:<5} | {:<10} | {:<10} | {:10} | {:20} '.format('', 'size', 'stock', 'price', 'variants'))
            for i, (size, stock, price, variant) in enumerate(zip(sz, stk, prc, vrnt)):
                print('{:<5} | {:<10} | {:<10} | {:10} | {:20} '.format(i, size, stock, '$'+price, variant))
            print('Total stock: {:<5}'.format(sum(ttl)))
        else:
            print('Stock could not be found :(')
            print('{:<5} | {:<10} | {:10} | {:20} '.format('', 'size', 'price', 'variants'))
            for i, (size, price, variant) in enumerate(zip(sz, prc, vrnt)):
                print('{:<5} | {:<10} | {:10} | {:20} '.format(i, size, '$'+price, variant))
    formatData()
    def ATC():
        print('')
        choice = input('Would you like to buy this item? (y/n) ')
        while (choice != 'y') and (choice != 'n'):
            choice = input('Would you like to buy this item? (y/n) ')
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
            print('Thanks for using shopify stock checker. Goodbye!')
            sys.exit()
        elif choice == 'n':
                choice1 = input('Would you like to input another link? (y/n) ')
                while (choice1 != 'y') and (choice1 != 'no'):
                    if choice1 == 'y':
                        continue
                    else:
                        print('Ok, closing shopify stock checker')
                        sys.exit()

    ATC()
