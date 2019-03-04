#acd = input("podaj stringa: ")


def middle(acd):
    length = len(acd)
    x = int(length / 2) + (length % 2) - 1
    print(length)
    return acd[x]
print(middle("test"))