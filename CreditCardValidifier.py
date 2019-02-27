#num = '51'
def credit(num):
    number_as_string = str(num)
    number_length = len(number_as_string)
    providers_list = ['VISA', 'MasterCard', 'AMEX', 'Discover', 'Invalid']
    #print(number_as_string[0])
    print(number_length)
    #print(number_as_string[]) in (51,55)
    #print((number_length == 13 or number_length == 16))
    #print(int("55") in (51, 55))
    #print(number_as_string[:2])
    #print('37' in (34, 37))
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

print(credit(4128374839283))

"""
Test.assert_equals(credit(6011364837263748), "Discover")
Test.assert_equals(credit(5318273647283745), "MasterCard")
Test.assert_equals(credit(12345678910), "Invalid")
Test.assert_equals(credit(371236473823676), "AMEX")
Test.assert_equals(credit(4128374839283), "VISA")
"""