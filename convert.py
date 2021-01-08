#from lxml import html
from bs4 import BeautifulSoup
import requests

def fetchstuff(index):
	page = requests.get('https://www.mcdonalds.com.sg/nutrition-calculator/#1+12')
	#tree = html.fromstring(page.content)
	soup = BeautifulSoup(page.content, 'html.parser')

	print(soup.prettify())

	#lis = tree.xpath('//li[@class="fact_energy"]')
	#print(tree)
	#print(lis)
	#for item in lis:
		#print(item.text)

fetchstuff(1)