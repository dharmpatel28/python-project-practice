weather = {}
array =[]
with open('3nyc_weather.csv', 'r') as rf:
    for element in rf:
        data=element.split(',')
        date = data[0] 
        temperature = int(data[1])
        weather[date] = temperature
        array.append(temperature)

# print(weather)

print(sum(array[0:7])/len(array[0:7]))
print(max(array[0:10]))
print(weather['1/9/2016'])