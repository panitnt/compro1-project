import json
from turtle import Turtle, Screen
from airline import Airline

turtle = Turtle()
screen = Screen()


def print_flight_num(num_flight_with_des):
    '''
    use to print flight number with route on the screen
    :param num_flight_with_des: str of flight number
    '''
    i, j, num = 0, 300, 0
    num_flight_des = list(num_flight_with_des.items())
    while num < len(num_flight_with_des):
        key, value = num_flight_des[num]
        turtle.penup()
        turtle.goto(i, j)
        turtle.pendown()
        style = ('Comic Sans MS', 30, 'normal')
        turtle.write(f'flight no.{key} : {value}', font=style, align='center')
        num += 1
        j -= 50


def enter_text_screen(x, y, text):
    '''
    use to print some text on screen
    :param x: int of position x
    :param y: int of position y
    :param text: str of text that want to show
    '''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    style = ('Comic Sans MS', 30, 'normal')
    turtle.write(f'{text}', font=style, align='center')


def print_menu_list():
    '''use to print flight that use function enter_text_screen to help'''
    enter_text_screen(0, 200, 'Press 1 to reserve seat')
    enter_text_screen(0, 100, 'Press 2 to cancel seat')
    enter_text_screen(0, 0, 'contact : Tel 000-000-0000')


def create_all_flight(num_flight_with_des, seat_file):
    '''
    to create json file of this flight
    :param num_flight_with_des: dict of flight number with route
    :param seat_file: str of text file name
    '''
    num_flight_all = list(num_flight_with_des.keys())
    try:
        with open(f'{num_flight_all[0]}.json', 'r') as flight_file:
            flight_data = json.load(flight_file)
    except FileNotFoundError:
        for i in range(len(num_flight_all)):
            num_flight = num_flight_all[i]
            c_airline = Airline(num_flight)
            c_airline.new_flight(seat_file)
