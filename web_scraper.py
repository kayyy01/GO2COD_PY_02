from bs4 import BeautifulSoup
import requests

url = "https://sempremilan.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = soup.find_all("h2")

    for index, headline in enumerate(headlines, start=1):
        print(f"Headline{index}:{headline.get_text(strip=True)}")
        
else:
    print(f"Falied to retrieve the webpage. Status code: {response.status_code}")        

