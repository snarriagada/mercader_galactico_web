

def is_traduction(list):
    if "I" in list:
        return True
    if "V" in list:
        return True
    if "X" in list:
        return True
    if "L" in list:
        return True
    if "C" in list:
        return True
    if "D" in list:
        return True
    if "M" in list:
        return True
    return False

def is_metal_price(list):
    if("silver" in list[0].lower()):
        return True
    if("gold" in list[0].lower()):
        return True
    if("iron" in list[0].lower()):
        return True
    return False

def is_conversion_question(list):
    if(list[0].lower() == "how much"):
        return True
    return False

def is_price_question(list):
    if(list[0].lower() == "how many credits"):
        return True
    return False

