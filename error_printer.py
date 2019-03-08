#examples:
# s="aaabbbbhaijjjm"
# error_printer(s) => "0/14"
#
# s="aaaxbbbbyyhwawiwjjjwwm"
# error_printer(s) => "8/22"


def printer_error(s):
    return str(len(['' + i for i in s if i not in "abcdefghijklm"])) + "/" + str(len(s))


print(printer_error("aaabbbbhaijjjmxxxx"))