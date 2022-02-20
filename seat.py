import json
from turtle import Turtle, Screen
from member import Member

turtle = Turtle()
screen = Screen()
screen.setup(width=700, height=900)


class Seat:
    def __init__(self, flight_json, member):
        '''
        Initialize Seat by
        :param flight_json: data in each flight in json type
        :param member: Member()
        '''
        self.flight_json = flight_json
        self.list_row_seat = [340, 305, 270, 235, 200, 165, 130, 95, 60, 25, -10, -45, -80, -115, -150, -185, -220,
                              -255, -290, -325]  # to get y position when show screen
        self.alpha_col = {'A': -240, 'B': -195, 'C': -150, 'D': -60, 'E': -15, 'F': 30, 'G': 75, 'H': 165, 'J': 210,
                          'K': 255}  # to get x position when show screen
        self.member = member

    @property
    def flight_json(self):
        '''get flight_json'''
        return self.__flight_json

    @flight_json.setter
    def flight_json(self, json_name):
        '''set flight_json'''
        if not isinstance(json_name, str):
            raise TypeError('flight_json use to be a file name of json')
        self.__flight_json = json_name

    @property
    def member(self):
        '''get member'''
        return self.__member

    @member.setter
    def member(self, member_class):
        '''set member'''
        if not isinstance(member_class, Member):
            raise TypeError('member use to be Member class')
        self.__member = member_class

    def head_table(self):
        '''to show row(alphabet) and column(number) in the screen'''
        turtle.pencolor('black')
        alpha_row = ['A', 'B', 'C', ' ', 'D', 'E', 'F', 'G', ' ', 'H', 'J', 'K']
        for i in range(len(alpha_row)):
            turtle.penup()
            turtle.goto(-240 + (i * 45), 370)
            turtle.pendown()
            turtle.write(alpha_row[i])
        i = 1
        while i <= 20:
            turtle.penup()
            turtle.goto(-300, 370 - (i * 35))
            turtle.pendown()
            turtle.write(f'{i}')
            i += 1

    def draw_rect(self, color, x, y):
        '''
        to show in each seat
        :param color: str of code color
        :param x: int of position in x
        :param y: int of position in y
        '''
        turtle.color(color)
        turtle.penup()
        turtle.goto(x, y)
        turtle.shape('square')
        turtle.shapesize(1, 1)
        turtle.stamp()

    def passenger_info_flight(self, flight, info):
        '''
        to update passenger info of this flight
        :param flight:
        :param info:
        '''
        try:
            with open(f'{flight}_passenger.json', 'r') as flight_passenger_info:
                passenger = json.load(flight_passenger_info)
        except FileNotFoundError:
            with open(f'{flight}_passenger.json', 'w') as flight_passenger_info:
                json.dump(info, flight_passenger_info, indent=4)
        else:
            passenger.update(info)
            with open(f'{flight}_passenger.json', 'w') as flight_passenger_info:
                json.dump(passenger, flight_passenger_info, indent=4)
