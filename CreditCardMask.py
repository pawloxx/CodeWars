"""
Your task is to write a function maskify, which changes all but the last four characters into '#'
"""

# return masked string
#input
cc = 'input'
#masking function
def maskify(cc):
    mask = '#'*(len(cc) - 4) + cc[-4:]
    return mask

#just check
print(maskify(cc))