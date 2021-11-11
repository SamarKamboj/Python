from random import randint

num = []
ascOrder = []   # ascOrder --> Ascending Order 

for i in range(10):
    num.append(randint(1, 100)) 
while num:
    maximum = 100
    for x in num:
        if maximum > x:
            maximum = x
    ascOrder.append(maximum)
    num.remove(maximum)

def mean():
    meanValue = 0
    for x in ascOrder:
        meanValue += x

    meanValue = meanValue / len(ascOrder)
    return "The mean of this list is " + str(meanValue)


def median():
    # If total number in list are even 
    firstPosi = int(len(ascOrder)/2)
    secondPosi = int((len(ascOrder)/2) + 1)
    firstValue = ascOrder[firstPosi-1]
    secondValue = ascOrder[secondPosi-1]
    return "The median in this list is " + str((firstValue + secondValue)/2)


def Mode():
    modeValue = max(ascOrder, key=ascOrder.count)
    return "The mode in this list is " + str(modeValue) + "   " + "*Disclaimer: If there is no mode in this list then it will show the first value of this list. But it is also possible that the mode is actually be the value that is on first place."


print(ascOrder)

print(mean())

print(median())

print(Mode())