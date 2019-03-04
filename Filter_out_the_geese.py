#function should return list of elements without elements from birds(list)

#birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
#geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    list_last = [name for name in birds if name not in geese]
    return list_last
