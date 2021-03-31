import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com')

contacts = ['Bianca Schmitt', 'Vo Braganey', 'Vó Braganey', 'Mãe tim', 'Pai Tim']
contains_emoticon = True

messageInput = sys.argv[1]
print('Message: ', messageInput)

if not messageInput:
    message = 'Boom dia :finger'
else:
    message = messageInput     
    

if not sys.argv[2]:
    contains_emoticon = False
else:
    contains_emoticon = True

time.sleep(5)

def find_contact(contact):
    field_search = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    field_search.click()

    field_search.send_keys(contact)
    field_search.send_keys(Keys.ENTER)

def send_message(message, contains_emoticon: bool):
    fields = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    
    field_search = fields[1]
    
    field_search.click()
    field_search.send_keys(message)

    time.sleep(15)

    field_search.send_keys(Keys.ENTER)
    time.sleep(5)
    if contains_emoticon:
        field_search.send_keys(Keys.ENTER)


for contact in contacts:
    find_contact(contact)
    
    time.sleep(5)
    
    send_message(message, contains_emoticon)




