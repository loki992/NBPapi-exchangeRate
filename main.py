import requests
import json

choice = "y"
while choice.lower()!="e":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    print('1. Podaj symbol waluty której kurs chcesz sprawdzić: np "USD"')
    print('2. Aby wyświetlić listę walut wpisz - "l"')
    print('3. Aby zakończyć wpisz - "e"')
    choice = input("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    if choice.lower() == "l":
        print(""" bat (Tajlandia)	1 THB
dolar amerykański	1 USD
dolar australijski	1 AUD
dolar Hongkongu	1 HKD
dolar kanadyjski	1 CAD
dolar nowozelandzki	1 NZD
dolar singapurski	1 SGD
euro	1 EUR
forint (Węgry)	100 HUF
frank szwajcarski	1 CHF
funt szterling	1 GBP
hrywna (Ukraina)	1 UAH
jen (Japonia)	100 JPY
korona czeska	1 CZK
korona duńska	1 DKK
korona islandzka	100 ISK
korona norweska	1 NOK
korona szwedzka	1 SEK
lej rumuński	1 RON
lew (Bułgaria)	1 BGN
lira turecka	1 TRY
nowy izraelski szekel	1 ILS
peso chilijskie	100 CLP
peso filipińskie	1 PHP
peso meksykańskie	1 MXN
rand (Republika Południowej Afryki)	1 ZAR
real (Brazylia)	1 BRL
ringgit (Malezja)	1 MYR
rupia indonezyjska	10000 IDR
rupia indyjska	100 INR
won południowokoreański	100 KRW
yuan renminbi (Chiny)	1 CNY
SDR (MFW)	1 XDR""")
    elif (choice.lower() == "e"):
        input("Wcisnij enter aby zakończyć")
        print("Dzięki i do zobaczenia :)")
        exit()
    else:
        symbol = choice
        base_api = "http://api.nbp.pl/api/"
        option = "/exchangerates/rates/c/"
        api_url = base_api + option + symbol+"/today/"
        response = requests.get(api_url)
        if str(response)=="<Response [404]>":
            print("nbp nie podaje tych wartosci dla tej waluty lub wystapil inny problem")
        else:
            response_dict = response.json()
            print(f"Wybrana waluta to: {response_dict['currency']}")
            print(f"Aktualny kurs kupna w stosunku do zlotówki to {response_dict['rates'][0]['bid']} PLN za 1 {response_dict['code']}")
            print(f"Kurs sprzedaży wynosi {response_dict['rates'][0]['ask']} PLN za 1 {response_dict['code']}")