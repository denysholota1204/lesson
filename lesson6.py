#iterable = list('Python')
#first_element = iterable[0]
#second_element = iterable[1]
#last_element = iterable[-1]
#print(iterable)
#print(first_element)
#print(second_element)
#print(last_element)


#my_list = [1, 66, 8, 30 , 0, 2]
#extension = [[4, 6, 8, 3, 2]]
#print(my_list)
#last_element_of_second_list = my_list[2][2][0]
#print(last_element_of_second_list)

#list_2 = list('ddgdg')
#print(list_2)

#my_list.clear()
#print(my_list)

#my_list.pop(1)

#my_list.insert(2, 5)

#my_list.sort(reverse=True)

#my_list.extend(extension)

#print(my_list)

#print(len(my_list))

#copy_list = my_list.copy()

#print(copy_list)

#if 66 in my_list:
#    print('Okay')
#else:
#    print('Bad')

#for element in sorted(my_list):
#    print(element)

goods = ['Bananas', 'Milk', 'Tomatoes', 'Apples', 'Water', 'Breads']
sold_goods = []

while True:
    match = input('\nВітаю в системі магазину!\nДля показу всіх товарів натисніть 1.\nДля постачання товарів натисніть 2.\nДля продажу натисніть 3\nДля виводу проданих товарів за день натисніть 4\nДля перегляду історії продажів натисніть 5')
    if match == '0':
        print('Thank you!')
        break
    elif match == '1':
        for good in goods:
            print(good)
    elif match == '2':
        print('Products delivery')
        product = input('Enter the product you would like to delivery: ')
        goods.append(product)
    elif match == '3':
        print('Selling product')
        product = input('Enter the product you would like to buy: ')
        goods.remove(product)
        sold_goods.append(product)
    elif match == '4':
        for good in sold_goods:
            print(good)
    elif match == '5':
        for good in sold_goods.reverse():
            print(good)

