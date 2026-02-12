stocks={}
with open('2hash.csv', 'r') as rf:
    for data in rf:
        elements=data.split(',')
        day = elements[0]
        price = elements[1]
        stocks[day]=price
print(stocks)
print(stocks['March 7'])