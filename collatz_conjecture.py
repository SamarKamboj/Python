import matplotlib.pyplot as plt

x = [*range(1, 10001)]
y = []

for i in x:
    a = i
    steps = 0

    while a != 1:
        if a%2 == 0:
            a /= 2
            steps += 1
        elif a%2 != 0:
            a = (a*3)+1
            steps += 1

    y.append(steps)

plt.scatter(x, y, label='circle', color='red', marker='*', s=25)
plt.xlabel('Integer ---->')
plt.ylabel('Steps occured ---->')
plt.title('Collatz Conjecture')
plt.show()
