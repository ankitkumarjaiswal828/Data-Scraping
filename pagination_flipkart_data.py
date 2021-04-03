from bs4 import BeautifulSoup
import requests
import csv

headers = {'uers_Agent':'Mozilla/5.0, (Windows NT 10.0 ; Win64 ;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

laptop_name =[]
laptop_price =[]
ratings = []
#processors =[]
pages = list(range(1,26))
for page in pages:
    sources = requests.get('https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}'.format(page),headers = headers).text
    soup = BeautifulSoup(sources,'html.parser')
    #print(soup.prettify())

    for names in  soup.find_all('div',class_="_4rR01T"):
        laptop_name.append(names.text)

    for price in soup.find_all('div',class_="_30jeq3 _1_WHN1"):
        laptop_price.append(price.text)
        print(len(laptop_price))
    for rate in soup.find_all('div',class_="_3LWZlK"):
        ratings.append(rate.text)
'''
    pro = soup.find_all('li',class_="rgWa7D")
    for i in range(0,len(pro)):
        p = pro[i].text
        if "Core" in p:
            processors.append(p)
'''


filename = "pagination_filpkart_data.csv"

with open(filename,'w',encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Serial_no',"Laptop_name","Laptop_price","laptops_rating","laptop_processors"])

    for i in range(len(laptop_name)):
        writer.writerow([i,laptop_name[i],laptop_price[i],ratings[i]])
