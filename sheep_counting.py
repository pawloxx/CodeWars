#input = non-negative intiger,3 output: "1 sheep...2 sheep...3 sheep..."
n = 3
def count_sheep(n):
    y = ""
    for sheep in range(1, n+1):
        y += ("".join((str(sheep), " sheep...")))
    return y
print(count_sheep(n))