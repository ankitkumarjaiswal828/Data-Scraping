from selenium import webdriver
import pandas as pd
import time
import os
path = os.getcwd()
chromedriver = 'chromedriver'
driver_path = os.path.join(path, chromedriver)
driver = webdriver.Chrome(driver_path)
driver.get('https://www.justdial.com')
driver.maximize_window()

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#time.sleep(5)

driver.find_elements_by_xpath('//*[@id="ht_lk_sub_1_11"]')
lo = input('Enter You Want to be City:')
r =driver.find_element_by_id('srchb').is_displayed()
print(r)
req = driver.find_element_by_xpath('//*[@id="srchbx"]')
re = input('Enter Your Requirments :')
driver.find_element_by_xpath('//*[@id="srIconwpr"]').click()

'''def strings_to_num(argument):
    switcher = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    }
    return switcher.get(argument, "nothing")

storeDetails = driver.find_elements_by_class_name('store-details')
nameList = []
addressList = []
numbersList = []
for i in range(len(storeDetails)):
    name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
    address = storeDetails[i].find_element_by_class_name('cont_fl_addr').get_attribute('innerHTML')
    contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
    myList = []
    for j in range(len(contactList)):
        myString = contactList[j].get_attribute('class').split("-")[1]
        myList.append(strings_to_num(myString))
    nameList.append(name)
    addressList.append(address)
    numbersList.append("".join(myList))

data = {'Company Name': nameList,
        'Address': addressList,
        'Phone':numbersList}

# Create DataFrame
df = pd.DataFrame(data)
print(df)
print(df.to_csv('Restaurants_data.csv'))'''
#driver.quit()
