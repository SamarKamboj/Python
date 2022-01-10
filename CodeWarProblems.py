def divisors(integer):
    Divisors = []
    for i in range(2, integer):
        if integer%i == 0:
            Divisors.append(i)
    if len(Divisors) == 0:
        return f"{integer} is prime"
    return Divisors


def order(sentence):
    emList = sentence.split()
    emList2 = []
    for x in range(1, len(emList)+1):
        for i in emList:
            if f"{x}" in i:
                emList2.append(i)
    return ' '.join(emList2)


def find_next_square(sq):
    main = sq**0.5
    if str(main)[-1] != '0':
        return -1
    return (main+1)**2


def longest(a1, a2):
    new = list(a1 + a2)
    char = ''
    for x in new:
        if x in a1 and x not in char:
            char += x
        if x in a2 and x not in char:
            char += x
    return ''.join(sorted(char))

# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))


def accum(s):
    List1 = list((s.lower()))
    List2 = []
    for i in List1:
        char = ''
        for _ in range(List1.index(i)+1):
            char += i
        List2.append(char.capitalize())
    List2 = "-".join(List2)
    return (List2)

print(accum("HbideVbxncC"))