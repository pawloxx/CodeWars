my_string = "blah, lots  ,  of ,  spaces, here,n bbbbb ggggg    +  "
result = [x.strip() for x in my_string.split(',')]
print(result)