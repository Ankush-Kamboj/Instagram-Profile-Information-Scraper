import requests
from bs4 import BeautifulSoup

username = input("Enter Instagram username: ")

response = requests.get('https://instagram.com/' + username)
soup = BeautifulSoup(response.text, 'html.parser')
user_info = soup.find("meta", property="og:description")

clean_user_info = user_info.attrs['content'].split('-')[0]
print(clean_user_info)