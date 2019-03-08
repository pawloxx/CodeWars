# Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.
#
# (In this case, all triangles must have surface greater than 0 to be accepted).


def is_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

print(is_triangle(1,2,3))



# better way
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)