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

print(credit(num))