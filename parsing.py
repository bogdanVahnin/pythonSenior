import requests

response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')

#print(responce.text)

response_parse = response.text.split('Долар США')
response_parse = response_parse[1].split('</td')
response_parse = response_parse[1].split('>')
US_dollar = response_parse[-1]

print(US_dollar)