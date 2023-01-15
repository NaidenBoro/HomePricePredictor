import requests
import json

#x = requests.get('https://www.homes.bg/api/offers?startIndex=0&stopIndex=0')

#json.loads(x.text)['result']
appartaments = []

#Retriving all the appartaments
for i in range (140):
    x = requests.get('https://www.homes.bg/api/offers?startIndex=%s&stopIndex=%d' % (i, i+99))
    appartaments = appartaments+json.loads(x.text)['result']
    print(i)


#Formating the data in a more readable format
f = open("data.csv", "a",encoding="utf-8")
for ap in appartaments:
    
    if(ap['price']['currency'] != 'EUR'):
        continue
    str = ap['location'] + ',' + ap['title'] + ',' + ap['description'].replace(',','+')+',' + ap['price']['value'].replace(',','')+'\n'
    str=str.replace(' ','')
    str=str.replace('m²','')
    f.write(str)
f.close()