# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

from pprint import pprint

def format_duration(seconds):
    if (seconds == 0):
        return 'now'

    years = seconds//31536000
    days = (seconds - years*31536000)//86400
    hours = (seconds - years*31536000 - days*86400)//3600
    minutes = (seconds - years*31536000 - days*86400 - hours*3600)//60
    seconds = seconds - years*31536000 - days*86400 - hours*3600 - minutes*60

    res = [years, days, hours, minutes, seconds]
    res_dict = dict(zip(["year","day","hour","minute","second"],res))

    res_string = ""

    # need to get the number of null value inside the dict
    null_counter = 0
    for key, val in res_dict.items():
        if (val == 0):
            null_counter += 1


    # iterate again...
    counter = 0
    for key, val in res_dict.items():

        if (val == 0):
            pass

        else:

            # if only one value to display, easy
            if (null_counter == 4):
                if (val > 1):
                    return "{} {}".format(val, key+"s")
                else:
                    return "{} {}".format(val, key)

            # need to keep track if that the latest non null item to add or not
            counter += 1
            if (5 - counter == null_counter):
                res_string = res_string[:-2]
                if (val > 1):
                    res_string += " and {} {}, ".format(val, key+"s")
                else:
                    res_string += " and {} {}, ".format(val, key)

            else:
                if (val > 1):
                    res_string += "{} {}, ".format(val, key+"s")
                else:
                    res_string += "{} {}, ".format(val, key)
        
    return res_string[:-2]



# print(format_duration(15731080))
# print(format_duration(62))
# print(format_duration(120))
# print(format_duration(3600))
# print(format_duration(3662))

"""
* (very) clever but possible !!

times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
"""
    


