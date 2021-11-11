from random import randint

num = []  # --> Empty list
# 'num' list in ascending order
ascOrder = []   # ascOrder --> Ascending Order 
# If range is even then total numbers are even else odd.
for i in range(10):  
   num.append(randint(1, 100))
# Arrange in ascending order or we can use sort() in-built function.
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

    meanValue = round(meanValue / len(ascOrder), 1)
    return "The mean of this list is " + str(meanValue)


def median():
    # For Even
    if len(ascOrder) % 2 == 0:
        x = int(len(ascOrder)/2)
        y = int((len(ascOrder)/2) + 1)
        firstValue = ascOrder[x-1]
        secondValue = ascOrder[y-1]
        return "The median in this list is " + str((firstValue + secondValue)/2)
    # For Odd
    else:
        z = int((len(ascOrder)/2) + 1)
        value = ascOrder[z-1]
        return "The median in this list is " + str(value)


def Mode():
    modeValue = max(ascOrder, key=ascOrder.count)
    return "The mode in this list is " + str(modeValue) + "   " + "*Disclaimer: If there is no mode in this list then it will show the first value of this list. But it is also possible that the mode is actually be the value that is on first place."


print(ascOrder)

print(mean())

print(median())

print(Mode())
