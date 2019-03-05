

def middle(r):
    if len(r) == 0:
        return ""
    elif len(r) % 2 != 0:
        return r[len(r)//2]
    elif len(r) % 2 == 0:
        return r[len(r)//2 - 1] + r[len(r)//2]

print(middle("1234"))