from bs4 import BeautifulSoup
import requests
import csv
headers = {'uers_Agent':'Mozilla/5.0, (Windows NT 10.0 ; Win64 ;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

mypage = requests.get('https://www.amazon.in/s?k=mobiles&ref=nb_sb_noss_2',headers = headers).text
soup = BeautifulSoup(mypage , 'lxml')
#print(soup.prettify())

phone_names = []
phones_price = []

for names in soup.find_all('span',class_ ='a-size-medium a-color-base a-text-normal'):
    string = names.text
    phone_names.append(string.strip())

for price in soup.find_all('span',class_ = 'a-price-whole'):
    phones_price.append(price.text)

file_name = 'phone_details.csv'

with open(file_name , 'w') as file:
    write = csv.writer(file)
    write.writerow(['Sr.no','Phone_names','Phones_price'])

    for i in range(len(phone_names)):
        write.writerow([i,phone_names[i],phones_price[i]])
