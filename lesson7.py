import random
#my_list = [1, 66, 8, 30, 2, 2, 2]
#sum = 1

#for element in my_list:
#    sum *= element

#print(max(my_list))

#my_list = ['abc', 'xyz', 'aba', '1221']

#count = 0

#for element in my_list:
#   if len(element) >= 2 and element[0] == element[-1]:
#       print(element)
#        count += 1

#rint(count)

#a = [1,2,3,4,5]
#b = [5,6,7,8,9]

#result = False
#for i in a:
#    for j in b:
#        if i == j:
#            result = True
#            break

#print(result)

#while True:
#    name = input('Enter your name')
#    if name:
#        break
#    else:
#        print('Імя не введено')


#random_number = random.randint(0,5)

#while True:
#    guess = int(input('Try tu guess from 0 to 5: '))
#    if guess == random_number:
#        print('You are right!')
#        break
#    else:
#        print('Please try again!')


#name = input('Enter your name: ')
#surname = input('Enter your surname: ')

#a = 0
#b = 0
#for element in name:
#    a += 1
#for element in surname:
#    b += 1
#print(f'name {a}, surname {b}')


my_list = [1, 2, [3, 4, 7, 3, 1, 3, 6, 8, 0]]
for element in my_list:
    if type(element) == list:
        element.sort()

tmp = my_list[-1]
my_list.pop(-1)

my_list.sort()
my_list.extend([tmp])

print(my_list)


 
    


