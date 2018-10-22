import random


def swap(l, i1, i2):
    tmp = i1
    if i1 > i2:
        i1 = i2
        i2 = tmp
    first = l.pop(i1)
    second = l.pop(i2-1)
    l.insert(i1, second)
    l.insert(i2, first)


l = [random.randint(0, 1000) for _ in range(200)]
s = [1, 5, 3, 0, 7]
print(s)
swap(s, 0, len(s)-1)
print(s)
swap(s, 2, 3)
print(s)
swap(s, 1, 3)
print(s)
swap(s, len(s)-1, 2)
print(s)
