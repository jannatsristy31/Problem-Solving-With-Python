class Flight:
    def __init__(self, flight_no, departure, arrival, d_time, a_time, capacity):
        self.flight_no = flight_no
        self.departure = departure
        self.arrival = arrival
        self.d_time = d_time
        self.a_time = a_time
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if self.capacity > len(self.passengers):
            self.passengers.append(passenger)


class Passenger:
    def __init__(self, name, phone_no, passport_no):
        self.name = name
        self.phone_no = phone_no
        self.passport_no = passport_no
        self.flight = []

    def add_flight(self, flight):
        if flight.flight_no in self.flight:
            print("This flight is already booked.")
        else:
            self.flight.append(flight)
            print("Booking Successful!")

    def remove_flight(self, flight):
        if flight.flight_no in self.flight:
            self.flight.remove(flight)
            print("Booking cancelled successfully!")


class Booking:
    # def __init__(self):
    #     self.flights = {}

    def book_flight(self, flight_no, departure, arrival, d_time, a_time, capacity):
        return Flight(flight_no, departure, arrival, d_time, a_time, capacity)

    def cancel_booking(self, passenger):
        passenger.remove_flight(self)


    def view_flights(self):



