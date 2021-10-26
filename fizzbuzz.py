emptyList = []
for x in range(1, 101):
  if x % 15 == 0:
    emptyList.append('FizzBuzz')
  elif x % 3 == 0:
    emptyList.append('Fizz')
  elif x % 5 == 0:
    emptyList.append('Buzz')
  else:
    emptyList.append(x)
print(emptyList)