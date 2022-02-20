from turtle import Screen
from data_list import price_flight
from airline import Airline
from member import Member
from seat import Seat

screen = Screen()


class Flight:
    def __init__(self, airline, member, seat):
        '''
        Initialize with parameter airline, member, and seat
        :param airline: Airline()
        :param member: Member()
        :param seat: Seat()
        '''
        self.airline = airline
        self.seat = seat
        self.member = member

    @property
    def airline(self):
        '''get airline'''
        return self.__airline

    @airline.setter
    def airline(self, airline_set):
        '''set airline'''
        if not isinstance(airline_set, Airline):
            raise TypeError('airline use to be an Airline class')
        self.__airline = airline_set

    @property
    def member(self):
        '''get member'''
        return self.__member

    @member.setter
    def member(self, member_set):
        '''set member'''
        if not isinstance(member_set, Member):
            raise TypeError('member use to be an Member class')
        self.__member = member_set

    @property
    def seat(self):
        '''get seat'''
        return self.__seat

    @seat.setter
    def seat(self, seat_set):
        '''set seat'''
        if not isinstance(seat_set, Seat):
            raise TypeError('seat use to be an Seat class')
        self.__seat = seat_set

    def show_seat(self):
        '''to show all seat (which available or not) into screen'''
        # show empty
        self.seat.head_table()  # head table
        seat_plan = self.airline.read_seat()
        seat = list(seat_plan.keys())
        reserve_or_not = list(seat_plan.values())
        for i in range(len(seat)):
            row, column = int(seat[i][:-1]), seat[i][-1]
            get_pos_x, get_pos_y = self.seat.alpha_col[f'{column}'], self.seat.list_row_seat[row - 1]
            if reserve_or_not[i] != 'N':
                color = '#7B6079'
            elif row <= 3:
                color = '#DE8971'
            elif row <= 7:
                color = '#A7D0CD'
            else:
                color = '#90AACB'
            self.seat.draw_rect(color=color, x=get_pos_x, y=get_pos_y)  # to show seat

    def reserve(self):
        '''to get which seat that passenger want to reserved and have payment
        in this function. Finally, update in json file that this seat have already reserved'''
        # what seat you want
        want_seat = screen.textinput(title='Choose seat do you want', prompt=f'economy - blue\n'
                                                                             f'business - green\nfirst - orange\n'
                                                                             f'press column and row ex. 11A')
        status_seat = self.airline.read_seat()
        # to get seat that want to reserve and not key error. If key error, it will try to input again
        while True:
            try:
                check_seat = status_seat[want_seat]
            except KeyError:
                print('Please try in form column and row ex. 11A')
                want_seat = screen.textinput(title='Choose seat do you want', prompt=f'economy - blue\n'
                                                                                     f'business - green\n'
                                                                                     f'first - orange\n'
                                                                                     f'press column and row ex. 11A')
            else:
                break
        # to check that have already to reserved or not
        if check_seat == 'N':
            # if not it will use Member class to get information and payment
            reserve_member = self.member.member_info()
            self.member.payment(want_seat, 'seat_plan.txt', price_flight('ticket_price.txt'),
                                self.airline.flight_num)
            confirm = screen.textinput(title='Confirm your seat', prompt=f'confirm seat {want_seat} (y to confirm) ')
            if confirm.lower() == 'y':
                # if you confirm, it will update to screen
                try:
                    want_row, want_column = int(want_seat[:-1]), want_seat[-1].upper()
                except ValueError:
                    print(f'Error to reserve seat {want_seat}, Please try again')
                except AttributeError:
                    pass
                else:
                    want_pos_x = self.seat.alpha_col[f'{want_column}']
                    want_pos_y = self.seat.list_row_seat[want_row - 1]
                    self.seat.draw_rect(color='#7B6079', x=want_pos_x, y=want_pos_y)
                    self.airline.update_flight(want_seat, reserve_member)
                    passenger_info = self.member.member_all_info
                    self.seat.passenger_info_flight(self.airline.flight_num, passenger_info)
            else:
                print(f'Error to reserve seat {want_seat}, Please try again')
        else:
            print('This seat already reserved, Please try again')

    def cancel_seat(self):
        '''to get which seat that passenger want to canceled. Finally, update in json file that
        this seat have already benn canceled'''
        # to get firstname
        while True:
            firstname = screen.textinput(title='Enter to cancel seat', prompt='Enter your firstname')
            if type(firstname) != str or firstname == '':
                print('Please enter passport ID again')
            else:
                break
        # to get last name
        while True:
            lastname = screen.textinput(title='Enter to cancel seat', prompt='Enter your lastname')
            if type(lastname) != str or lastname == '':
                print('Please enter passport ID again')
            else:
                break
        firstname_up = firstname[0].upper() + firstname[1:len(firstname)]
        lastname_up = lastname[0].upper() + lastname[1:len(lastname)]
        name = lastname_up + firstname_up
        # to get seat that want to cancel
        seat_cancel = screen.textinput(title='Enter to cancel seat', prompt='Enter your seat that want to cancel')
        status_seat = self.airline.read_seat()
        try:
            check_name = status_seat[seat_cancel]
        except KeyError:
            print('Error, please try again')
        else:
            if check_name == name:
                # if same name, it will cancel but not show on screen immediately
                self.airline.update_flight(seat_cancel, 'N')
                passenger_info = self.member.member_all_info
                passenger_info[check_name] = 'cancel seat'
                self.seat.passenger_info_flight(self.airline.flight_num, passenger_info)
                print('Already accept, it will take 0-7 days to cancel')
            else:
                # if not if will tell you to try again
                print('Cancel Error, please try again')
