from bs4 import BeautifulSoup
import requests

#Step 1 : Fetch the HTML Content from a URL
url = "https://www.example.com"
response = requests.get(url)

#Step 2 : Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

#Step3 : Extract data

#Get the title
print("Title", soup.title.string)


#Get all the links
for link in soup.find_all('a'):
    print("Link text",link.text.strip())
    print("URL",link.get("href"))