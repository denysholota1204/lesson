#name = input('Your name?:')
#city = input('Your city/town?:')
#age = input('Your age?')
#height = input('Your height?')


#print(f'My name is - {name}, i am from - {city} , my height - {height} ')

#x = int(input('x: '))
#y = int(input('y: '))

#if y >= 0:
 #   if x >=0:
#        print('I')
#    else:
#        print('II')
#else:
#   if x >= 0:
#        print('IV')
#    else:
#        print('III')


#a = float(input("Enter the side a: "))
#b = float(input("Enter the side b: "))
#c = float(input("Enter the side c: "))
#
#if a > 0 and b > 0 and c > 0:
#
#   if (a + b) > c and (a + c) > b and (c + b) > a:
#
#       print("This triangle exists")
#
#   else:
#
#       print("This triangle doesn't exist")
#
#else:
#
#    print("The side length can not be negative or equal to 0!")



#sum = 0
#for number in range(1, 100+1):
 #   if number % 2 !=0:
 #       print(number)
#        sum += number
#
#print('sum', sum)


#west = ['Antarctida', 'South America', 'North America',]

#a = west.extend(['Australia', 'Africa', 'Eurasia'])

#west.sort

#print(west)

#my_list = [['Andrii', 'Petrenko'], ['Petro', 'Ivanov'], ['Andrii', 'Nesterenko']]

#count = 0

#for element in my_list:
#    if element[0] == 'Andrii':
#        count += 1
    
#print(count)

#old_string = 'Hello evvvvery booooooody'

#space = old_string.find(' ')
#print(f'Space - {space}')

#if space == -1:
#    print('Word -', old_string)
#else:
#    word = old_string[:space]

    
#    while True:

#        new_space = old_string.find(' ', space+1)
#       new_word = old_string[space+1:new_space]
#        if len(word) < len(new_word):
#           word = new_word
#           new_string = print(old_string[space+1:])
#           if len(new_string.split()) == 0:
#              break
#           old_string = old_string[space+1:]
#print(word)

#months = (
#    1: 'January'
#    2: 'February'
#    3: 'March'
#    4: 'April'
#    5: 'May'
#)
 
#print(months)

#monthes = {1:  'січень',
        #  2:  'лютий',
        #   3:  'березень',
        # 4:  'квітень',
        #  5:  'травень',
        #   6:  'червень',
        #   7:  'липень',
        #   8:  'серпень',
        #   9:  'вересень',
        #   10: 'жовтень',
        #   11: 'листтопад',
        #   12: 'грудень'}

#report_date = '21.05.2022'

#month = report_date[3:5]

#print(month)


#grades = {
#    "Kiril": 2,
#   "Irina": 5,
#    "Matvii": 3,
#    "Denis": 4
#}
 
#good_grades = dict()

#for student_name, grade in grades.items():
#    if grade >= 4:
#        good_grades[student_name] = grade

#print(good_grades)


#forecast = {
#    "Kyiv":25,
#    "Cherkasy": 27,
#    "Odesa": 30,
#    "Donetsk": 26
#}
#
#total_temperature = 0
#count = len(forecast)
#
#for temp in forecast.values():
#    total_temperature += temp
#
#print(f'Avg of temperatures = {total_temperature/count}')


#surname = input('Enter your surname: ')
#counter = dict()

#for char in surname:
#    counter[char] = surname.count(char)

#print(counter.items())
#print(list(counter.items()))
#most_common = max(list(counter.items()), key=lambda x: x[1])

#most_common = max(list(counter,items()), key=lambda x: x[1])
#print(most_common[0])


#text = input('Enter: ')
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#for char in text:
#    if char in numbers:
#        text = text.replace(char, '')

#print(text)

