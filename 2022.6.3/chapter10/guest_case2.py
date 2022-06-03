filename = "text_files/guest_book.txt"

prompt = "\nEnter your name (Enter 'quit' to end the program): "

while True:
    name = input(prompt)

    if name == 'quit':
        break

    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')
