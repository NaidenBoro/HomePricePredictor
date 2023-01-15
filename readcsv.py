import csv

#Generating vocabularys
kv = []
stai = []
info = []
with open('data.csv', newline='',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        info=info+row[4].split('+')
        kv.append(row[0])
        stai.append(row[2])


kv = list(set(kv))
stai = set(stai)
stai.remove('Гараж')
stai = list(stai)
info =list(set(info))

# print(kv)
# print(stai)
# print(info)

#Generating a list of values to one hot encode a category based on a vocabulary of values
def one_hot(el, lst):
    result = [0] * len(lst)
    result[lst.index(el)] = 1
    return result


# Same thing but for multiple categories
def tokenize(elements, lst):
    result = [0] * len(lst)
    for el in elements:
        result[lst.index(el)] = 1
    return result


spr=','

# This is if you want to predict your own home or a new one

# my_home = 'Център,София,Тристаен,80,Обзаведен+Тухла+ТЕЦ'.split(',')
# output = spr.join(str(x) for x in one_hot(my_home[0],kv))+spr
# output += spr.join(str(x) for x in one_hot(my_home[2],stai))+spr
# output += my_home[3] + spr
# output += spr.join(str(x) for x in tokenize(my_home[4].split('+'),info))+spr
# output += my_home[5]
# print (output)

#Generating a proccessed csv without Garages

f = open("proccessed.csv", "a",encoding="utf-8")
with open('data.csv', newline='',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row[2] != 'Гараж':
            output = spr.join(str(x) for x in one_hot(row[0],kv))+spr
            output += spr.join(str(x) for x in one_hot(row[2],stai))+spr
            output += row[3] + spr
            output += spr.join(str(x) for x in tokenize(row[4].split('+'),info))+spr
            output += row[5]
            f.write(output+"\n")
f.close()
