from bs4 import BeautifulSoup as bs
import requests
import csv


headers = {'uers_Agent':'Mozilla/5.0, (Windows NT 10.0 ; Win64 ;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

source = requests.get('https://elpaso.craigslist.org/search/mcy?sort=date',headers = headers).text
soup = bs(source,'lxml')
#print(soup.prettify())

B_name = []
B_price =[]
b_posted_date =[]
Bike_urls =[]

for i in soup.find_all('a',class_ = 'result-title hdrlnk'):
    B_name.append(i.text)


for j in soup.find_all('time',class_='result-date'):
    b_posted_date.append(j.text)


for k in soup.find_all('span',class_ = 'result-price'):
    B_price.append(k.text)

for link in soup.find_all('a',class_="result-title hdrlnk"):
    Bike_urls.append(link['href'])
    #print(Bike_urls)

for pic in soup.find_all('div',class_="slider-info"):
    print(pic.text)

filename = 'Bike_details.csv'
with open(filename,'w',encoding ='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['serial_no','Bike_Name','Bike_Price','Bike_posted_date','Bike_urls'])

    for i in range(len(B_name)):
        writer.writerow([i,B_name[i],B_price[i],b_posted_date[i],Bike_urls[i]])
