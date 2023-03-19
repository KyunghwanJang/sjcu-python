file = open("test.txt", "w")
for data in range(1,11):
    file.write(f'{data} Line');
file.close()

file = open("test.txt", "r")
while True:
    Line = file.readline()
    if not Line:
        break
    print(Line)
file.close

file = open("test.txt", "a")
for data in range(1, 11):
    file.write(f'{data} Line\n');
file.close()

file = open("test.txt", "r")
lines = file.readline()
for line in lines:
    print(line)
file.close()

file = open("test.txt", "r")
data = file.read()
print(data)
file.close()
