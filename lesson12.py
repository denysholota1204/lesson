#numbers = {
#    "one": 1,
#    "two": 2,
#    "three": 3
#}
#
#for key in numbers.keys():
#    numbers[key] = numbers[key]*2
#
#print(numbers)


transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
}

transport['II6767AQ'] = 'Петренко Петро'
transport['CA8888CE'] = 'Іванов Олексій'

car_plate = input('Enter the place to find car owner: ')

car_owner = transport.get(car_plate, 'Not found' )
print('Car owner of plate {} is {}'.format(car_plate, car_owner))

car_owners = dict()

# {'Ivanov': 1, 'Petrov': 2}

for owner in transport.values():
    if car_owners.get(owner, 0) == 0:
        car_owners[owner] = 1
    else:
        auto_count = car_owners[owner]
        auto_count += 1
        car_owners[owner] = auto_count

for owner, auto_count in car_owners.items():
    if auto_count > 1:
        print(f'Owner {owner} has {auto_count} cars')
