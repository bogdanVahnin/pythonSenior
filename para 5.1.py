import requests
from bs4 import BeautifulSoup
'''coin_list = []
response = requests.get("https://coinmarketcap.com/")
print(response.status_code)
response.parse = response.text.split("<span>")
#print(response.parse)
for parse_elem in response.parse:
    if parse_elem.startswith('$'):
        for parse_elem2 in parse_elem.split("</span>"):
            if parse_elem2.startswith("$"):
                coin_list.append(parse_elem2.split("$")[1])
                print(parse_elem2)

print(coin_list)

bitcoin = coin_list[0].replace(',','')
print(bitcoin)'''

response = requests.get("https://coinmarketcap.com/currencies/hamster-kombat/")
soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all("span",{"class","sc-65e7f566-0 clvjgF base-text"})
print(soup_list)
res = str(soup_list[0]).split('>')
res = res[1].split('<')[0]
print("Hamster Kombat -",res)