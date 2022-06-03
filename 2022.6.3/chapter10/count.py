filename = 'text_files/alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
    count = contents.lower().count('the')
    print("number of 'the' in " + filename + ": " + str(count))
