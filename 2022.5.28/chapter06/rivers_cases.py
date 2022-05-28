rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'chang jiang': 'china',
}

for name, country in rivers.items():
    print("The " + name.title() + " runs through "
          + country.title() + ".")
