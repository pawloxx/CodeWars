"""
Make a program that sees if a credit card number is valid or not.
Also the program should tell you what type of credit card it is if it is valid.
The five things you should consider in your program is: AMEX, Discover, VISA, Master, and Invalid :
Discover starts with 6011 and has 16 digits,
AMEX starts with 34 or 37 and has 15 digits,
Master Card starts with 51-55 and has 16 digits,
VISA starts with 4 and has 13 or 16 digits.


"""
def credit(num):
    number_as_string = str(num)
    number_length = len(number_as_string)
    providers_list = ['VISA', 'MasterCard', 'AMEX', 'Discover', 'Invalid']

#VISA
    if (number_as_string[0] == '4' and (number_length == 13 or number_length == 16)):
        return providers_list[0]
#MasterCard
    elif int(number_as_string[:2]) in range(51, 56) and number_length == 16:
        return providers_list[1]
#AMEX
    elif int(number_as_string[:2]) in (34, 37) and number_length == 15:
        return providers_list[2]
#Discover
    elif number_as_string[:4] == '6011' and number_length == 16:
        return providers_list[3]
#Invalid
    else:
        return providers_list[4]
"""
assert(credit(6011364837263748), "Discover")
assert(credit(5318273647283745), "MasterCard")
assert(credit(12345678910), "Invalid")
assert(credit(371236473823676), "AMEX")
assert(credit(4128374839283), "VISA")
"""