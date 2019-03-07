def nb_year(p0, percent, aug, p):
    licznik = 0
    x = p0
    while True:
        licznik += 1
        y = round(x * percent/100) + aug
        c = x + y
        x += y
        if c >= p:
            break
    return licznik
print(nb_year(1000, 2, 50, 1200))


#policzyć ilość iteracji potrzebnych aby n1 był większy od p1

#BEST PRACTICE:

def nb_year_best(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year