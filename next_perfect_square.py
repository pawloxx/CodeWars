from math import pow, sqrt


def find_next_square(sq):
    if sq == 0:
        return -1
    elif sq % sq**0.5 == 0:
        return int(pow(sqrt(sq)+1, 2))
    else:
        return -1
print(find_next_square(0))