f,s = map(int,input().split())

def a(s, f):
    count = 0
    while s != f:
        if f % 2 == 0 and f//2 >= s:
            f //= 2
        else:
            if f % 2 == 0 and  s >= f:
                f += 1
            else:
                f -= 1
        count += 1
    return count
a(s,f)
