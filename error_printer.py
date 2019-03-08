#examples:
# s="aaabbbbhaijjjm"
# error_printer(s) => "0/14"
#
# s="aaaxbbbbyyhwawiwjjjwwm"
# error_printer(s) => "8/22"


def printer_error(input_string):
    length_of_chars_not_in_string = len(['' + i for i in input_string if i not in "abcdefghijklm"])
    return "{0}/{1}".format(length_of_chars_not_in_string, (len(input_string)))


print(printer_error("aaabbbbhaijjjmxxxx"))