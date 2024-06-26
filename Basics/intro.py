first  = 0
second = 1

n = 4

print(first, second, end = " ")

for i in range(n):
    third = first + second
    print(third, end = " ")
    first = second
    second = third