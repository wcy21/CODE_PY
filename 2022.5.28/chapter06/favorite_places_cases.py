favorite_places = {
    'alice': {
        'wonderland'
    },
    'blue_dog': {
        'china',
        'japan',
        'london',
    },
    'doctor': {
        'rhodes island',
        'ursus empire',
        'kazdel',
    }
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places:")
    for place in places:
        print("\t" + place.title())
