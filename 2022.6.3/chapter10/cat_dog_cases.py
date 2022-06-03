filenames = ['text_files/cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()

        print("\n--- " + filename + " ---")
        for line in lines:
            print(line.rstrip())

    except FileNotFoundError:
        pass
        # print("\nThe file '" + filename + "' does not exist.")
