# bin as list convertion to int


def binary_array_to_number(bin_as_list):
    converter = ''.join(str(i) for i in bin_as_list)
    return int(converter, 2)

print(binary_array_to_number([1,1,1,1]))