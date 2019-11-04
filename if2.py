sentence = input("Enter a sentence here: ")
sentence_without_space = ""

for i in sentence:
    if i != " ":
        sentence_without_space = sentence_without_space + i
    elif i == " ":
        continue

print(sentence_without_space)