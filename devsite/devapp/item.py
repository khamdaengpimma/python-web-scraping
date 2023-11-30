import requests
from bs4 import BeautifulSoup

url = "https://sachvuii.com/100-mau-chuyen-co-dong-tay/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class 'col-xs-6 col-md-3 col-sm-3' under the 'ebook' class
items = soup.find(class_='panel-body')
# Create a list to store the extracted information
result_list = {}
title = items.find(class_="ebook_title text-primary").getText()
img = items.find('img')['src']
link = items.find('a')['href']
text = items.get_text(strip=True)

#     # Add link and text to the result list
result_list={'title':title,'img':img,'link': link, 'text': text}

# Print or do further processing with the result_list
print(result_list)