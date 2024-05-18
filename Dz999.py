import requests
response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
text = response.text
parse = text.split('<td data-label="Офіційний курс">')

result = []

for item in parse:
    for value in item.split('</td>'):
        if value[1].isdigit():
            result.append(value)
print(f'USD cost -- {result[4]}')
Go = result[4]
how_many = int(input('How many UAH --'))

print(how_many / set)
