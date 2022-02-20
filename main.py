from turtle import Screen
from airline import Airline
from flight import Flight
from member import Member
from seat import Seat
from data_list import num_flight_with_des
from other_function import print_flight_num, print_menu_list, enter_text_screen, create_all_flight

screen = Screen()

# start program
create_all_flight(num_flight_with_des('ticket_price.txt'), 'seat_plan.txt')
while True:
    screen.setup(width=700, height=900)
    screen.bgpic('bg.gif')
    # choose menu of this program
    while True:
        enter_text_screen(0, 300, 'Welcome to Python Airlines')
        print_menu_list()
        menu_key = ['1', '2', 'E', 'e']
        menu = screen.textinput(title='Please choose menu',
                                prompt='If not, please contact via the channels mentioned. : enter E to exit')
        if menu in menu_key:
            screen.clearscreen()
            break
        print('Please try to enter menu again')
    if menu == 'E' or menu == 'e':
        break
    # choose flight
    while True:
        screen.bgpic('bg.gif')
        num_with_des = num_flight_with_des('ticket_price.txt')
        print_flight_num(num_with_des)
        choose_flight_key = [x for x in num_with_des.keys()]
        choose_flight_key.append('E')
        choose_flight_key.append('e')
        choose_flight = screen.textinput(title='Please choose flight', prompt='If not have, you can enter E to exit')
        if choose_flight in choose_flight_key:
            break
        print('Please try to choose flight again')
    if choose_flight == 'E' or choose_flight == 'e':
        break
    # to get in menu
    screen.clearscreen()
    screen.bgpic('bg2.gif')
    c_airline = Airline(choose_flight)
    c_flight = Flight(c_airline, Member(), Seat(f'{choose_flight}.json', Member()))
    c_flight.show_seat()
    if menu == '1':
        while True:
            c_flight.reserve()
            redo1 = screen.textinput(title='Press E to exit',
                                     prompt='Do you want to reserve again\nother flight please exit and get new start')
            if redo1 == 'E' or redo1 == 'e':
                break
    elif menu == '2':
        while True:
            c_flight.cancel_seat()
            redo2 = screen.textinput(title='Press E to exit',
                                     prompt='Do you want to cancel again\nother flight please exit and get new start')
            if redo2 == 'E' or redo2 == 'e':
                break
    redo = screen.textinput(title='Press E to exit',
                            prompt='Do you want to reserve/cancel again\nother flight please exit and get new start')
    screen.clearscreen()
    if redo == 'e' or redo == 'E':
        break
