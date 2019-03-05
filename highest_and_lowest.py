# high_and_low("1 2 3 4 5")  # return "5 1"
def high_and_low(s):
    splitowane = s.split(" ")
    return(max(splitowane, key = int)+" "+min(splitowane, key = int))


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))