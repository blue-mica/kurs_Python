import requests


def pobierz(link, sciezka):

    response = requests.get(link)
    print(response.status_code)
    if response.status_code == 200:

        bajty = 0

        try:
            with open(sciezka, 'wb') as plik:
                for part in response.iter_content(100000):
                    ilosc = plik.write(part)
                    bajty += ilosc
        except FileNotFoundError:
            bajty = 99999

        print(f"zapisano {bajty} bajtow")


def main():
    link = "http://junkee.com/wp-content/uploads/2017/11/Navy-Penis-Skywritting.jpg"
    pobierz(link, "us_navy.jpg")

if __name__ == "__main__":
    main()
