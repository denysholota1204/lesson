#clients = [
#    ['White House', 'Іванов', 3],
#    ['Shelter','Іванова', 5 ],
#    ['Верховина','Іванова', 5],
#    ['Буковель','Іванова',5]
#]
#
#hotels = dict()
#
#for vouncher in clients:
#    vouncher_hotel = vouncher[0]
#    vouncher_clients = vouncher[2]
#
#    if hotels.get(vouncher_hotel, 0) == 0:
#        hotels[vouncher_hotel] = vouncher_clients
#    else:
#        hotel_clients = hotels[vouncher_hotel]
#        hotels[vouncher_hotel] = hotel_clients + vouncher_hotel
#
#for hotel,clients in hotels.items():
#    print(f'У готелі {hotel} наразі проживає {clients} клієнтів')

def say_hello():
    print('Hello, World <3')