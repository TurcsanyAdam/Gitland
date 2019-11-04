ideabank = open("ideabank.txt", "r+")

num_lines = 0

for i in ideabank.readlines():
    num_lines += 1

ideabank = open("ideabank.txt", "r+")

print(ideabank.read())

ideabank = open("ideabank.txt", "a")

idea = input("Enter your new idea here: ")
ideabank.write("\n" + str(num_lines) + "." + idea)

ideabank.close()