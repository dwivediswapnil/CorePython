string = "python IS A PROGRAMMING language"
new_string = []
for i in string:
    if i.isupper():
        new_string.append(i.lower())
    else:
        new_string.append(i.upper())

print("".join(new_string))            