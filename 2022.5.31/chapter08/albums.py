def make_album(singer_name, album_name):
    album = {'singer': singer_name, 'name': album_name}
    return album


while True:
    print("\nPlease tell me about an album:")
    print("(enter 'q' at any time to quit)")

    singer = input("Singer name: ")
    if singer == 'q':
        break

    name = input("Album name: ")
    if name == 'q':
        break

    new_album = make_album(singer, name)
    print(new_album)

# album = make_album('Jay', 'Eight Dimensions', song_number=10)
# print(album)
#
# album = make_album('Michael Jackson', 'Dangerous')
# print(album)
#
# album = make_album('Yonedzu Kenshi', 'BOOTLEG', song_number=14)
# print(album)
