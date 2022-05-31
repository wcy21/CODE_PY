def show_magicians(magicians):
    print("\nHere are some of the names of magicians:")
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []

    for magician in magicians:
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    return great_magicians


magicians = ['LuChen', 'Eric', 'Franz Harary', 'David Copperfield']
great_magicians = []

great_magicians = make_great(magicians)
show_magicians(magicians)
show_magicians(great_magicians)
