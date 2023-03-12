#text = 'lorem impsum dolor sit amet'

#chars_counter = dict()
#for char in text:
#    if char != ' ':
#        if char not in chars_counter:
#                chars_counter[char] = text.count(char)

#print(chars_counter)

#counter_list = sorted(list(chars_counter.items()), key =lambda x: x[1])
#counter_list.reverse()
#print(counter_list)

#for element in counter_list[:3]:
#     print(f'{element[0]} - {element[1]}')


def func(a, b=2, c=3):
    print(f'a = {a}, b = {b}, c = {c}')

func(c=8, a=3)