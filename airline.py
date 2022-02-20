import json
from data_list import seat_dict


class Airline:
    def __init__(self, flight_num):
        '''
        Initialize flight in this airline with
        :param flight_num: str of flight number
        '''
        self.flight_num = flight_num

    @property
    def flight_num(self):
        '''get flight_num'''
        return self.__flight_num

    @flight_num.setter
    def flight_num(self, num_flight):
        '''set flight_num'''
        if not isinstance(num_flight, str):
            raise TypeError('flight num need to be string')
        self.__flight_num = num_flight

    def new_flight(self, seat_file):
        '''
        to create new flight seat from seat_plan.txt and update to json file
        :param seat_file: str of seat file name
        '''
        create_flight, seat_class = seat_dict(seat_file)
        add_flight = {
            self.flight_num: create_flight
        }
        # add this flight into json file
        try:
            with open(f'{self.flight_num}.json', 'r') as flight_data:
                flight = json.load(flight_data)
        except FileNotFoundError:
            with open(f'{self.flight_num}.json', 'w') as flight_data:
                json.dump(add_flight, flight_data, indent=4)
        else:
            flight.update(add_flight)
            with open(f'{self.flight_num}.json', 'w') as flight_data:
                json.dump(flight, flight_data, indent=4)

    def update_flight(self, seat, passenger):
        '''
        to update of who has reserved or canceled a seat.
        :param seat: str of seat number
        :param passenger: str of passenger name or 'N'(which have canceled)
        '''
        with open(f'{self.flight_num}.json', 'r') as flight_data:
            flight = json.load(flight_data)
        flight_seat = flight[f'{self.flight_num}']
        flight_seat[seat] = passenger
        with open(f'{self.flight_num}.json', 'w') as flight_data:
            json.dump(flight, flight_data, indent=4)

    def read_seat(self):
        '''to check if a seat has already been reserved or not'''
        with open(f'{self.flight_num}.json', 'r') as data_flight:
            seat_status = json.load(data_flight)
        flight_seat = seat_status[f'{self.flight_num}']
        # got dict which seat available or not
        return flight_seat
