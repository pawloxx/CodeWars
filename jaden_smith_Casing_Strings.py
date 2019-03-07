# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def toJadenCase(string):
    x = string.split()
    return ' '.join([i[0][0].upper()+i[1:] for i in x])

print(toJadenCase("How can mirrors be real if our eyes aren't real"))