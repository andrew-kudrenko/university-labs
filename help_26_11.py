file = open("assets/I will not betray myself.txt")
file2 = open("assets/result.txt", "w")

lines = file.readlines()
last_string = lines[-1:]

print(last_string)

for i, row in enumerate(lines):
    file2.write(lines[len(lines) - i - 1])

file.close()
file2.close()
