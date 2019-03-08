# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


def filter_list(input_list):
    return [i for i in input_list if type(i) is not str]

print(filter_list([1,2,'aasf','1','123',123]))

