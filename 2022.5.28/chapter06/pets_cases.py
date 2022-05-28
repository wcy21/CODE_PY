pets = {
    'asdaf': {
        'type': 'huskies',
        'master': 'eafew',
    },
    'eerqd': {
        'type': 'border collie',
        'master': 'fdsa',
    },
    'dcdzx': {
        'type': 'samoyed',
        'master': 'afddvx',
    },
}

for name, dog_info in pets.items():
    print("\nDog's name: " + name.title())
    for key, value in dog_info.items():
        print("\t" + key.title() + ": " + value.title())
