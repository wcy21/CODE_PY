people = {
    'Amiya': {
        'height': '142 cm',
        'birth': '12月23日',
        'city': '雷姆必拓',
    },
    'Eyjafjalla': {
        'height': '145 cm',
        'birth': '10月18日',
        'city': '莱塔尼亚',
    },
    'W': {
        'height': '165 cm',
        'birth': '本人表示遗忘',
        'city': '卡兹戴尔',
    },
}

for name, information in people.items():
    print("\nname: " + name)

    for key, value in information.items():
        print("\t" + key + ": " + value)
