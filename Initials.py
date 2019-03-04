# input - name surname
# output - n.s

#name = "Xavier Ren"
def abbrevName(name):
    names_list = name.split()
    initials = ""
    for x in names_list:
        initials += x[0]
    return (((".").join(initials)).upper())
#print(abbrevName(name))