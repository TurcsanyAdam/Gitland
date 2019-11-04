sentence = input("Enter a sentence here: ")
space_count = 0

for i in sentence:
    if i == " ":
        space_count = space_count + 1

print(space_count)