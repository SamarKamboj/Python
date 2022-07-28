def main():
    for _ in range(int(input())):
        print(solve())


def solve():
    
    arr_len = int(input())
    arr = [int(i) for i in input().split()]


    while True:
        s = 0
        for i in range(arr_len-1):
            smaller = 0
            for j in range(1+i, arr_len):
                if arr[i] & arr[j] != 0:
                    smaller = j if arr[j] < arr[i] else smaller

            if i < smaller:
                arr[i], arr[smaller]= arr[smaller], arr[i]
                s += 1

        if s == 0:
            break

    if sorted(arr) == arr:
        return "Yes"

    return "No"
    

main()
