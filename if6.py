sentence = "<Gabor> és Denes <fel>masztak <a diofa>ra"
sentence2 = ""
write = True

for i in sentence:
    if i == "<":
        write = True
    if i == ">":
        write = False
    if write == True:
        sentence2 = sentence2 + i
for i in sentence2:
    if i == "<":
        sentence2 = sentence2.replace(i, "\n")

print(sentence2)