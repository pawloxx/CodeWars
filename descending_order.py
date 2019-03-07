# Input: 21445 Output: 54421


def descending_order(num):
    sorted_ints = sorted([int(d) for d in str(num)], reverse=True)
    strings = [str(l) for l in sorted_ints]
    return int(''.join(strings))


print(descending_order(0))