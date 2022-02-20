def seat_dict(txt_file):
    '''
    to get dictionary about reserved or not and class of seat
    :param txt_file: str of text file name
    :return: 2 of dict
    '''
    seat_plan_file = open(txt_file).read().splitlines()
    seat_plan = [x for x in seat_plan_file[1:len(seat_plan_file)]]
    column_seat = {0: 'A', 1: 'B', 2: 'C', 5: 'D', 6: 'E', 7: 'F', 8: 'G', 11: 'H', 12: 'J', 13: 'K'}
    new_flight = {}
    seat_class = {}
    for row in range(len(seat_plan)):
        for column in range(len(seat_plan[row])):
            if seat_plan[row][column] == 'F':
                seat_alpha = column_seat[column]
                new_flight[f'{row + 1}{seat_alpha}'] = 'N'
                seat_class[f'{row + 1}{seat_alpha}'] = 'first'
            elif seat_plan[row][column] == 'B':
                seat_alpha = column_seat[column]
                new_flight[f'{row + 1}{seat_alpha}'] = 'N'
                seat_class[f'{row + 1}{seat_alpha}'] = 'business'
            elif seat_plan[row][column] == 'X':
                seat_alpha = column_seat[column]
                new_flight[f'{row + 1}{seat_alpha}'] = 'N'
                seat_class[f'{row + 1}{seat_alpha}'] = 'economy'
    return new_flight, seat_class


def price_flight(ticket_file):
    '''
    to get price in each seat class
    :param ticket_file: str of text file name
    :return: dict of ticket_price
    '''
    price_chart = open(ticket_file).read().splitlines()
    all_price_list = [x.split(',') for x in price_chart[1:]]  # 0flight,1class,2price,3where
    ticket_price = {}
    for i in range(len(all_price_list)):
        flight_no, seat_class, price, to_des = all_price_list[i]
        if flight_no not in ticket_price:
            ticket_price[flight_no] = {}
        price_dict_flight = ticket_price[flight_no]
        price_dict_flight[seat_class] = price
    return ticket_price


def num_flight_with_des(ticket_file):
    '''
    to get dictionary of flight number(keys) with route(values)
    :param ticket_file: str of text file name
    :return: dict of flight number with route
    '''
    price_chart = open(ticket_file).read().splitlines()
    all_price_list = [x.split(',') for x in price_chart[1:]]  # 0flight,1class,2price,3where
    flight_with_des = {}
    for i in range(len(all_price_list)):
        flight_no, seat_class, price, to_des = all_price_list[i]
        if flight_no not in flight_with_des:
            flight_with_des[flight_no] = to_des
    return flight_with_des
