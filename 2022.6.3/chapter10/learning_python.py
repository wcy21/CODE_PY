filename = 'text_files/learning_python.txt'

print("\nFirst Reading:")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.strip())

print("\nSecond Reading:")
with open(filename) as file_object:
    for line in file_object.readlines():
        print(line.replace('Python', 'C').strip())

print("\nThird Reading:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
