"""

Discover starts with 6011 and has 16 digits,
AMEX starts with 34 or 37 and has 15 digits,
Master Card starts with 51-55 and has 16 digits,
VISA starts with 4 and has 13 or 16 digits.

possible results | describe:

Discover | Discover starts with 6011 and has 16 digits,
AMEX | AMEX starts with 34 or 37 and has 15 digits,
Master Card | Master Card starts with 51-55 and has 16 digits,
VISA | VISA starts with 4 and has 13 or 16 digits.
Invalid | others than above

Discover - długość = 16
print("Twój numer karty to :", len(num[:1]),"\nDługość", val)

"""

num = '1111'
def credit(num):
    val = len(num)
    li = ['VISA', 'MasterCard', 'AMEX', 'Discover', 'Invalid']
#VISA
    if num[:1] == '4' and (val == 13 or val == 16):
        return li[0]
#MasterCard
    elif int(num[2]) in (51,55) and val == 16:
        return li[1]
#AMEX
    elif (num[:2] == '34' or num[:2] == '37') and val == 16:
        return li[2]
#Discover
    elif num[:4] == '6011' and val == 16:
        return li[3]
#Invalid
    else:
        return li[4]

credit(num)