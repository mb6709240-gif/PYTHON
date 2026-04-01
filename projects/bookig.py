movie = input("Enter movie name: ")
price = int(input("Enter ticket price: "))
seats = int(input("Enter available seats: "))

tickets = int(input("Enter number of tickets: "))

if tickets <= seats:
    total = tickets * price
    print("\nMovie:", movie)
    print("Tickets:", tickets)
    print("Total Amount:", total)
    print("Booking Successful!")
else:
    print("Not enough seats!")
