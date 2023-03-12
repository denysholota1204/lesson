
#my_string = 'Lorem ipsum dolor sit amet,\n consectetur adipiscing elit.\n Aliquam malesuada, est vitae suscipit vestibulum,'
#new_string = 'Lorem ipsum dolor sit amet,\n consectetur adipiscing elit.\n Aliquam malesuada, est vitae suscipit vestibulum,'
#n = int(input())
#n = int(input())
#if n > len(my_string):
#    print('Wrong input!')
#else:
#    new_string - my_string[n:]
#    print(new_string)


#s = 'I am learning strings in Python, Some new methods got now'
#sentences = s.split('.')
#print(sentences)


#a = input('Enter the sting: ')
#print(f'Symbols - {len(a)}')
#b = a.split()
#print(b)
#print(f'Words - {len(b)}')

#sentences = ["I am learning strings in Python.some new metods got now "]
#text = ', '.join(sentences)

#print(text)

#clean = '    spacious;    '.strip()
#print(clean)

#dog_text = "All dogs bark like dogs"
#cat_text = dog_text.replace('dogs', 'cats')
#print(cat_text)

#map = {ord('з'): 'z', ord('ю'): 'u'}
#transalated = 'зю'.translate(map)

#print(transalated)

delimiter = '-' * 80
goods = [['Апельсин', 6, 150], ['Лимон', 8, 90], ['Картопля', 123, 445]]
total_sum = 0
number = 0

print(delimiter)
print("|{:^5}|{:<40}|{:>15}| {:>14}|".format('#', 'Товар', "Кількість", "Вартість"))
print(delimiter)

for good in goods:
    name = good[0]
    amount = good[1]
    money = good[2]
    number += 1
    total_sum += money
    print("|{:^5}|{:<40}|{:>15}|{:>15}|".format(number, name, amount, money))

print(delimiter)
print("|{:<62}|{:>15}|".format(' Total:', total_sum))
print(delimiter)