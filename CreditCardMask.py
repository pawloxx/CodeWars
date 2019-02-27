# return masked string
#input
cc = 'asdasdasdasdsad'
#masking function
def maskify(cc):
    mask = '#'*(len(cc) - 4) + cc[-4:]
    return mask

#just check
print(maskify(cc))