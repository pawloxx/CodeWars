# square every digit of a number. f.e. 9119 = 811181


def square_digits(num):
    #x = [int(i)**2 for i in list(str(num))]
    return int(''.join(map(str, [int(i)**2 for i in list(str(num))])))


print(square_digits(9119))