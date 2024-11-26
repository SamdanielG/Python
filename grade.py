def grade_to_gpa(grade):
    switcher = {
            'A':4.0,
            'B':3.0,
            'c':2.0,
            'd':1.0,
            'e':0.0,
            }
    return switcher.get(grade,"invalid grade")
print(grade_to_gpa('a'))
print(grade_to_gpa('d'))