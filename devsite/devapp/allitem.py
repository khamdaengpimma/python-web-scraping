import requests
from bs4 import BeautifulSoup

url = "https://sachvuii.com/co-tich-than-thoai/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class 'col-xs-6 col-md-3 col-sm-3' under the 'ebook' class
items = soup.find_all(class_='col-xs-6 col-md-3 col-sm-3 ebook')
# Create a list to store the extracted information
result_list = []

# Iterate through the found elements
for item in items:
    # Extract link and text
    img = item.find('img')['src']
    link = item.find('a')['href']
    text = item.get_text(strip=True)

    # Add link and text to the result list
    result_list.append({'img':img,'link': link, 'text': text})

# Print or do further processing with the result_list
print(result_list)
