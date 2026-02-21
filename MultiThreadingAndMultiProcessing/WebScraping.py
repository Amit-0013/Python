import threading
import requests
from bs4 import BeautifulSoup
urls = ['https://www.geeksforgeeks.org/python/python-programming-language-tutorial/',
        'https://www.w3schools.com/python/'
        ]
def fetch_contains(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Length of content in {url} is {len(soup.text)}")
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_contains,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()