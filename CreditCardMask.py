
def maskify(cc):
    mask = '#'*(len(cc) - 4) + cc[-4:]
    print(mask)
    return mask

