import requests
from bs4 import BeautifulSoup

adres = "http://trojmiasto.pl/"

response = requests.get(adres)

print(response.status_code)

response.raise_for_status()

trojmiasto_zupa = BeautifulSoup(response.text, "html.parser")

linki = trojmiasto_zupa.select(".news-list a")
# print(linki)

for link in linki:
    # print(link.getText())
    # print(link.attrs)
    # print(link.attrs)

    print(f"Wiadomosc: {link.get('title')}")
    print(link.get("href"))
    print("--------------\n")