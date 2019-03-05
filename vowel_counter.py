#test.assert_equals(getCount("abracadabra"), 5)
def vowel_counter(s):
    x = list(s.replace(" ", ""))
    y = ["a", "o", "i", "u", "e"]
    c = 0
    for i in x:
        if i in y:
            c += 1
    return(c)
print(vowel_counter("voue ikgasf"))