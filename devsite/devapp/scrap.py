import requests
from bs4 import BeautifulSoup

def menu():
    url = "https://sachvuii.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(class_='cat-item col-xs-12 col-md-4 col-sm-6')
    result_list = []
    for item in items:
        # Extract link and text
        link = item.find('a')['href']
        text = item.get_text(strip=True)
        result_list.append({'link': link, 'text': text })
    return result_list

def category(url):
    result_list = []
    for i in range(1,20):
        response = requests.get(url+'page/'+str(i)+'/')
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all elements with class 'col-xs-6 col-md-3 col-sm-3' under the 'ebook' class
        items = soup.find_all(class_='col-xs-6 col-md-3 col-sm-3 ebook')
        if items==[]:
            break
        print(i)
        for item in items:
            # Extract link and text
            img = item.find('img')['src']
            link = item.find('a')['href']
            text = item.get_text(strip=True)
            result_list.append({'img':img,'link': link, 'text': text})

    # Print or do further processing with the result_list
    return result_list 
    return result_list
def bookone(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find(class_='panel-body')
    # Create a list to store the extracted information
    result_list = {}
    title = items.find(class_="ebook_title text-primary").getText()
    img = items.find('img')['src']
    link = items.find('a')['href']
    text = items.get_text(strip=True)

    #     # Add link and text to the result list
    result_list={'doc':url,'title':title,'img':img,'link': link, 'text': text}
    return result_list