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
    print("CONVERSION = ", conversion)
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

    print("Metals_price: ", metals_price)
    return metals_price
    
    # pish pish Iron is 3910 Credits
    # save_metal_price recibe:  ['pish pish Iron', '3910 Credits']
    # metals prices:  {'Silver': [['glob', 'glob'], '34 Credits'],
    # 'Gold': [['glob', 'prok'], '57800 Credits'], 'Iron': [['pish', 'pish'], '3910 Credits']}

def handle_questions(form_data, conversion, metals_price):
    output_lines = []
    question = form_data["question"].lower()
    question = question.split("\r\n")
    print("QUESTION: ",question)
    for q in question:
        q = q.split(" is ")
        if is_conversion_question(q):
            print("IS CONVERSION QUESTION")
            amount = q[1].split(" ")
            roman_number = galactic_to_roman(amount, conversion)
            result = roman_to_integer(roman_number)
            response = q[1][:-1]+"is "+str(result)
            output_lines.append(response)
        elif is_price_question(q):
            print("IS PRICE QUESTION")
            unit_prices = get_unit_metal_prices(metals_price, conversion)
            deal_price = get_deal_price(q[1], unit_prices, conversion)
            response = q[1][:-1]+"is "+str(deal_price)+" Credits"
            output_lines.append(response)

        else:
            output_lines.append("I have no idea what you are talking about")
            print("I HAVE NO IDEA WHAT YOU ARE TALKING ABOUT")

    print("output lines: ", output_lines)
    return output_lines
    
