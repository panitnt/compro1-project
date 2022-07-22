# Flyflight Project

by Panitta Tanyavichitkul 6410546181

## Project overview and features

### Overview

This project is about to reserve and cancel seat in flight. It can show that which seat that available and have already
reserved.It has 4 classes are Member, Airline, Flight, and Seat. It will be use more of json file and txt file to help
remember who reserve seat(include some information about this passenger). I will use turtle graphic to show that which
seat that available and have already reserve , and have screen.textinput to input. Most of them will all be connected by
json file.

### Features

Main features are reserved and cancel seat that have more features such as payment or input information inside

<a href='https://youtu.be/t11sb9eN_xU'>you can click here to see my video</a>

## Required libraries and tools

It will not use specific version of Python.

## Program design

This picture is about diagram of this program.

![screen](project%20diagram.png)

### 1. Airline()

`__init__`

- flight_num : str of flight number

`new_flight` to create new flight seat from seat_plan.txt and update to json file.

- seat_file : str of seat file name

`update_flight` to update of who has reserved or canceled a seat.

- seat : str of seat number
- passenger : str of passenger name or 'N'(which have canceled)

`read_seat` to check if a seat has already been reserved or not.

### 2. Flight()

`__init__`

- airline : Airline()
- member : Member()
- seat : Seat()

`show_seat` to show seat that has already been reserved or not in screen.

`reserve` to reserve seat that in this function have screen.textinput to input seat that you want to reserve and have
called Member class to get about passenger information. Finally, It will update that this seat has already reserved.

`cancel_seat` to cancel seat that in this function have screen.textinput to input seat number, firstname, and lastname
to ensure that this passenger is the same as the one who made the reservation. But it will not update now in screen.

### 3. Member()

`__init__` have empty dict inside

`payment` inside this function have random alphabet and number to check that you aren't robot. You need to input credit
card number (16-digit). Before check that you aren't robot, it will show price that you want to reserve.

- seat : str of seat number
- seat_file : str of seat_plan.txt name
- price_dict : dict of price in each class that from price_flight in data_list.py
- flight : str of flight number

`member_info` this function is about to get information about passenger from screen.textinput in append in to empty
dict(self) and return lastname+firstname.

### 4. Seat()

`head_table` to show row(alphabet) and column(number) in the screen

`draw_rect` to show in each seat

- color : str of color
- x : int of x-position in the screen
- y : int of y-position in the screen

`passenger_info_flight` to add passenger information to json file

- flight : str of flight number
- info : dict of passenger information

## Code structure

### main.py

Main.py is main to run this program.

### airline.py

Airline.py has a class called Airline() that is use to generate and edit flights.

### flight.py

Flight.py has a class called Flight() is main to reserve and cancel seat.

### member.py

Member.py has a class called Member() that is use about payment and get passenger information.

### seat.py

Seat.py has a class called Seat() that can show seat and update json file which has already been reserved.

### data_list.py

Data_list.py have 3 function to help to get information to use in this program.

- seat_dict : to get new_flight, which will be used to create in json file and seat_class dictionary, which can tell
  class about this seat
- price_flight : to get dictionary of ticket_price to use to get price in each class
- num_flight_with_des : to get dictionary of flight number(keys) and routh(values)

### other_function.py

- print_flight_num : use to print flight number with route on the screen
- enter_text_screen : use to print some text on screen
- print_menu_list : use to print flight that use function enter_text_screen to help
- create_all_flight : to create json file of this flight
