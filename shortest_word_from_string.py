#test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)

def find_shortest_word(s):
    list_of_strings = s.split()
    list_of_lens = []
    for word in list_of_strings:
        list_of_lens.append(len(word))
    return(min(list_of_lens))

print(find_shortest_word("L all go on holiday somewhere very cold"))