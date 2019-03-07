#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"


def longest(s1, s2):
    return ''.join(sorted(set((s1+s2))))

print(longest("aretheyhere", "yestheyarehere"))