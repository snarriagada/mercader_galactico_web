from .validations import *
from .conversions import *

def set_conversion_data(form_data):
    conversion = {}
    for number in form_data.keys():
        if number == "i" and form_data[number]:
            galactic = form_data[number]
            conversion[galactic] = "I"
        if number == "v" and form_data[number]:
            galactic = form_data[number]
            conversion[galactic] = "V"
        if number == "x" and form_data[number]:
            galactic = form_data[number]
            conversion[galactic] = "X"
        if number == "l" and form_data[number]:
            galactic = form_data[number]
            conversion[galactic] = "L"
        if number == "c" and form_data[number]:
            galactic = form_data[number]
            conversion[galactic] = "C"
        if number == "d" and form_data[number]:
            galactic = form_data[number]
            conversion[galactic] = "D"
        if number == "m" and form_data[number]:
            galactic = form_data[number]
            conversion[galactic] = "M"
    return conversion

def set_prices_data(form_data):
    metals_price = {}
    if form_data["gold"]:
        line = form_data["gold"]
        line = line.split(" is ")
        quantity = line[0]
        quantity = quantity.split(" ")
        if quantity[-1].lower() == "gold" : quantity.pop()
        metal = line[1]
        metals_price["gold"] = [quantity, metal]

    if form_data["silver"]:
        line = form_data["silver"]
        line = line.split(" is ")
        quantity = line[0]
        quantity = quantity.split(" ")
        if quantity[-1].lower() == "silver" : quantity.pop()
        metal = line[1]
        metals_price["silver"] = [quantity, metal]

    if form_data["iron"]:
        line = form_data["iron"]
        line = line.split(" is ")
        quantity = line[0]
        quantity = quantity.split(" ")
        if quantity[-1].lower() == "iron" : quantity.pop()
        metal = line[1]
        metals_price["iron"] = [quantity, metal]

    return metals_price

def handle_questions(form_data, conversion, metals_price):
    output_lines = []
    question = form_data["question"].lower()
    question = question.split("\r\n")
    for q in question:
        q = q.split(" is ")
        if is_conversion_question(q):
            amount = q[1].split(" ")
            roman_number = galactic_to_roman(amount, conversion)
            result = roman_to_integer(roman_number)
            response = q[1][:-1]+"is "+str(result)
            output_lines.append(response)
        elif is_price_question(q):
            unit_prices = get_unit_metal_prices(metals_price, conversion)
            deal_price = get_deal_price(q[1], unit_prices, conversion)
            response = q[1][:-1]+"is "+str(deal_price)+" Credits"
            output_lines.append(response)
        else:
            output_lines.append("I have no idea what you are talking about")

    return output_lines
    
