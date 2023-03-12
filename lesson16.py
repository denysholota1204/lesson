booking_book = {}

def booking(clients_name, amount=2):
    booking_book[clients_name] = amount
    print('Client {client_name}, booked {amount}-places table.')


booking('Holota')
booking('Petrenko', 4)

print(booking_book)