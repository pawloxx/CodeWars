duplet = [('Bobo', 'TOBO'), ('Tabi', 'SRABI')]
 #zamien mi to ktos
#'`Bobo` Tobo, `Tabi` SRABI'

def duplet_fn(duplet):
    l = []
    for x in duplet:
        for i in x:
            l.append(i)
    #print(len(l))

    l2 = []
    for index, s in enumerate(l):
        if index % 2 == 0:
            x = ("`" + s + "`")
            l2.append(x)
        else:
            y = s
            l2.append(y)


    string = ' '.join(l2)
#print(string)
    return string

print(duplet_fn(duplet))

assert (duplet_fn(('Bobo', 'TOBO'), ('Tabi', 'SRABI')) and