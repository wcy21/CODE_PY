filename = 'text_files/program_reason'

prompt = "\nEnter why you like programming:"
prompt += "\n(Enter 'quit' to quit) "

while True:
    reason = input(prompt)

    if reason == 'quit':
        break

    with open(filename, 'a') as file_object:
        file_object.write(reason + '\n')
