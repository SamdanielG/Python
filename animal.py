def animal_sound(animal):
    switcher= {
    'dog':'bark',
    'cat':'meow',
    'cow':'moo',
    'lion':'roar',
    }
    return switcher.get(animal,"unknown sound")
print(animal_sound('dog'))
print(animal_sound('cat'))
print(animal_sound('giraffe'))

            