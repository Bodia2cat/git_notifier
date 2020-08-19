from bs4 import BeautifulSoup
from lxml import html
import requests
import os
import notify2
import time

notify2.init("Test")

text = requests.get("https://github.com/Bodia2cat").text
# Beautiful Soup and find page
soup = BeautifulSoup(text)
count = soup.find('span', {'class': 'Counter'})
#need count to activate notigication
number_need = input("Number of lust repo in github: ")
count_need = '<span class="Counter" title="16">' + number_need + '</span>'

print("lolkek" + str(count))
print("lolkek" + str(count_need))

while True:
	if count_need == str(count):
		n = notify2.Notification("New repository on my github")
		n.show()
		time.sleep(10)