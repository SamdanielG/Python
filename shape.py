def shape_area(shape,dimension):
    if shape =='circle':
        return 3.14*(dimension**2)
    elif shape == 'square':
        return dimension**2
    elif shape == 'traiangle':
        return 0.5*dimension[0]*dimension[1]
    else:
        return"invalid shape"
print(shape_area('circle',5))
print(shape_area('square',4))
print(shape_area('traingle',(4,3)))
print(shape_area('hexagon',5))