# return True when ammount of x's == ammount of o's in string

def xo(s):
    a = s.lower()
    return a.count('x') == a.count('o')

print(xo("xxoox"))