#Mumble generator
#Input->Output: accum("abcd") -> "A-Bb-Ccc-Dddd"
#Input->Output: accum("cwAt") -> "C-Ww-Aaa-Tttt"


s = 'ZpglnRxqenU'


def accum(s):
    words = list(s)
    new_list = []
    for index, e in enumerate(words):
        new_list.append(e.upper()+(e.lower()*index))

    return("-".join(new_list))

print(accum(s))
#print(words_lenght)
#print("-".join(words).upper())
