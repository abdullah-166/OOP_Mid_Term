class Star_Cinema:
    def __init__(self) -> None:
        self.hall_list = []
        
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.seat = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.show_list.append(show)

        seat = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append('free')
            seat.append(row)
        
        self.seat[id] = seat


    def book_seats(self, id, seats):
            
        if id not in self.seat:
            raise ValueError("Invalid ID: ")
        
        for seat in seats:
            if seat[0] >= self.rows or seat[1] >= self.cols:
                raise ValueError("Invalid Seat Number: ")
        
        for seat in seats:
            if self.seat[id][seat[0]][seat[1]] != 'free':
                raise ValueError("This seat is already Booked")
            
        for seat in seats:
            self.seat[id][seat[0]][seat[1]] = 'booked'


    def view_show_list(self):

        for show in self.show_list:
            print(f'Movie name: {show[1]} ID NO: {show[0]} time: {show[2]}')
        
    
    def view_available_seats(self, id):

        if id not in self.seat:
            raise ValueError("Invalid ID")
        
        for row in self.seat[id]:
            print(row)

cinema = Star_Cinema()

hall = Hall(10, 10, 201)
cinema.entry_hall(hall)

hall.entry_show(101, "Life of Pie", "10.00 P.M")
hall.entry_show(102, "John wick Chapter: 1", "12.00 P.M")
hall.entry_show(103, "Jawan", "02.00 P.M")
hall.entry_show(104, "Dhaka Attack", "03.00 P.M")
hall.entry_show(105, "Operation Shundarban", "03.00 P.M")

while True:

    print("Choose an Option: ")
    print("1. View Show List.")
    print("2. View Avaliable Seats.")
    print("3. Book Seats.")
    print("4. Exit")
    
    choise = int(input("Enter an Option:"))
    print()

    if choise == 1:

        print("____Today's Movie Lists______")
        print()
        hall.view_show_list()
        print()

    elif choise == 2:

        id = int(input("Enter Show ID:"))
        print()
        print(f'___Avaliabe Seats for ID {id} Given Below___')
        print()
        hall.view_available_seats(id)
        print()

    elif choise == 3:
        
        id = int(input("Enter Show ID:"))
        seats = []

        number_of_seat = int(input("How many seat you want to book:"))

        for i in range(number_of_seat):
            seat = input("Enter the row and column number of the seat (e.g  1,2): ").split(",")
            seats.append((int(seat[0]), int(seat[1])))
        
        try:
            hall.book_seats(id,seats)
        except ValueError as e:
            print(e)

        print()

    elif choise == 4:
        break

    else :
        print("Wrong choise")
