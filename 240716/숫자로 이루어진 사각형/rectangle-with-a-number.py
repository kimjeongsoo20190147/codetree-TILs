n = int(input())

def print_num(n):
    s = 1
    for _ in range(n):
        for _ in range(n):
            if s >= 10:
                s = 1
                print(s, end=" ")
                s += 1
            else:
                print(s, end=" ")
                s += 1
        print()

print_num(n)