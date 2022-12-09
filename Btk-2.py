             from random import randint
from random import shuffle

myList = [0, 1, 2, 3, 4, 5, 6]
for number in myList:
    print(number)

for number in list(range(15)):
    print(number * 5)

index = 0
for number in list(range(5, 12)):
    print(f"guncel numara: {number} ; index numarasi: {index}")
    index = index + 1

for eleman in enumerate(list(range(5, 10))):
    print(eleman)

#randit ile random sayi
print(randint(0,100))
print(myList[randint(0,9)])
#shuffle
myList2 = [12,11,10,9,8,7]
shuffle(myList2) #sayilari birbirine karistiriyor
print(myList2)

#zip
foodList = ["Muz","Ananas","Elma"]
caloriList = [120,100,80]
dayList = ["pazartesi","salı","cuma"]
ziple = list(zip(foodList,caloriList,dayList))
print(ziple)

#ileri liste
listeEx = []
myString = "Furkan"

for harf in myString:
    listeEx.append(harf)
print(listeEx)#1.yol

newListEx = [eleman for eleman in myString]#tek satirla for
print(newListEx)#2.yol
newList = [num*5 for num in list(range(0,10))]#tek satirla for
print(newList)
