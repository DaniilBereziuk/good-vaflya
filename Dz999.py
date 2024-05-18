import requests
response = requests.get('https://coinmarketcap.com/')
text = response.text
parse = text.split('<td data-label="Офіційний курс">')

result = []

for item in parse:
    for value in item.split('</td>'):
        if value[1].isdigit():
            result.append(value)

print(result)