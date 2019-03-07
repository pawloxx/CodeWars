# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case


def is_isogram(x):
    return len(x) == len(set(x.lower()))

print(is_isogram("moOse"))

