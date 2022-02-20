from turtle import Screen
from data_list import seat_dict
import random

screen = Screen()


class Member:
    def __init__(self):
        '''Initialize Member with empty dict'''
        self.member_all_info = {}

    def payment(self, seat, seat_file, price_dict, flight):
        '''
        payment function to show price and enter credit card number
        :param seat: str of seat number
        :param seat_file: txt file name
        :param price_dict: dict of price in each class
        :param flight: str of flight number
        '''
        alpha_up = ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'X']
        alpha_down = ['b', 'd', 'f', 'h', 'j', 'n', 'p', 'r', 't', 'v', 'y']
        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        choice = ['up', 'down', 'num']
        str_check = ''  # to get check that it's not robot
        for i in range(6):
            choose = random.choice(choice)
            if choose == 'up':
                str_check += random.choice(alpha_up)
            elif choose == 'down':
                str_check += random.choice(alpha_down)
            elif choose == 'num':
                str_check += str(random.choice(num))
        create_flight, seat_class = seat_dict(seat_file)
        this_seat_class = seat_class[seat]  # to get class of this seat
        price_this_flight = price_dict[flight]
        price = price_this_flight[this_seat_class]  # to get price of this seat
        while True:
            credit_card = screen.textinput(title='Enter your credit card number (16-num)',
                                           prompt=f'class:{this_seat_class} price:{price}')
            if len(credit_card) == 16:
                break
            print('credit card number error, please enter 16-digits')
        pw = screen.textinput(title='!!!!!!!!!', prompt=f'You will pay by credit number {credit_card}\n'
                                                        f'Please enter {str_check} to confirm')
        while pw != str_check:
            pw = screen.textinput(title='!!!!!!!!!', prompt=f'You will pay by credit number {credit_card}\n'
                                                            f'Please enter {str_check} to confirm')
        else:
            print('Payment Completed')

    def member_info(self):
        '''
        to get passenger info from screen.textinput
        :return: str of lastname + firstname
        '''
        while True:
            # to get prefix name
            while True:
                prefix = screen.textinput(title='Enter Member Information', prompt='Enter your name prefix')
                if type(prefix) != str or prefix == '':
                    print('Please enter prefix name again')
                else:
                    break
            # to get firstname
            while True:
                firstname = screen.textinput(title='Enter Member Information', prompt='Enter your firstname')
                if type(firstname) != str or firstname == '':
                    print('Please enter firstname again')
                else:
                    break
            # to get lastname
            while True:
                lastname = screen.textinput(title='Enter Member Information', prompt='Enter your lastname')
                if type(lastname) != str or lastname == '':
                    print('Please enter lastname again')
                else:
                    break
            # to get birthdate
            while True:
                birthday = screen.textinput(title='Enter Member Information', prompt='Enter your birthday(DDMMYYYY)')
                if len(birthday) == 8:
                    break
                else:
                    print('Please try in form DDMMYYYY again')
            # to get nationality
            while True:
                nationality = screen.textinput(title='Enter Member Information', prompt='Enter your nationality')
                if type(nationality) != str or nationality == '':
                    print('Please enter nationality again')
                else:
                    break
            # to get passport id
            while True:
                passport_id = screen.textinput(title='Enter Member Information', prompt='Enter your passport ID')
                if type(passport_id) != str or passport_id == '':
                    print('Please enter passport ID again')
                else:
                    break
            # to get Thai citizen id
            while True:
                thai_id = screen.textinput(title='Enter Member Information', prompt='Enter your Thai-national ID')
                if type(thai_id) != str or thai_id == '':
                    print('Please enter Thai-national ID again')
                else:
                    break
            firstname_up = firstname[0].upper() + firstname[1:len(firstname)]
            lastname_up = lastname[0].upper() + lastname[1:len(lastname)]
            # to confirm passenger information
            confirm = screen.textinput(title='Your member info',
                                       prompt=f'name : {prefix} {lastname_up + firstname_up}\n'
                                              f'birthday : {birthday}\nnationality : {nationality}\n'
                                              f'passport ID : {passport_id}\nThai-national ID : {thai_id}\n'
                                              f'please enter "yes" to confirm and enter redo(or other) to try again')
            if confirm == 'yes':
                break
            else:
                print('Please fill in again')
        # to update to list
        self.member_all_info[lastname_up + firstname_up] = {
            'prefix': prefix,
            'birthday': birthday,
            'nationality': nationality,
            'passport_id': passport_id,
            'thai_id': thai_id
        }
        return lastname_up + firstname_up
