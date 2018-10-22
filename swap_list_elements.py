import random
import dis


def swap(l, i1, i2):
    tmp = i1
    if i1 > i2:
        i1 = i2
        i2 = tmp
    first = l.pop(i1)
    second = l.pop(i2-1)
    l.insert(i1, second)
    l.insert(i2, first)


def py_swap(l, i1, i2):
    l[i1], l[i2] = l[i2], l[i1]


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
print()
print(s)
py_swap(s, 3, 1)
print(s)
py_swap(s, 0, 4)
print(s)

print()
print('swap():')
dis.dis(swap)
print('py_swap():')
dis.dis(py_swap)