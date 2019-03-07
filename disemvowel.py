# return a string without vowels, 'y' is not vowel this time


def disemvowel(string):
    #vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return ''.join([w for w in string if w.lower() not in 'aeiou'])
print(disemvowel("This website is for losers LOL!"))