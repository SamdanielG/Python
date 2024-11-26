def day_of_week(day_number):
    switcher = {
    1:"sunday",
    2:"monday",
    3:"tuesday",
    4:"wednesday",
    5:"thursday",
    6:"friday",
    7:"saturday",
            }
    return switcher .get(day_number,"invalid day number")
print(day_of_week(3))
print(day_of_week(8))             