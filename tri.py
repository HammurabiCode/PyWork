# coding=utf-8

def tri():
    l = [1]
    while True:
        yield l
        l = [1] + [l[i + 1] + l[i] for i in range(0, len(l) - 1)] + [1]
        # l.append(0)
        # l = [l[i-1] + l[i] for i in range(0, len(l))]
        # l = [0] + l + [0]
        # l =


print range(1, 0)
g = tri()
n = 0
while n < 10:
    n = n + 1
    print next(g)
