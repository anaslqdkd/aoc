file = open("day15.txt")
line = file.readline()
line = line.strip('\n')

def hash(line):
    if line == []:
        return 0
    current = 0
    for char in line:
        ascii_code = ord(char)
        current += ascii_code
        current *= 17
        current %= 256
    return current

string = 'HASH'
lst = list(string)
print(lst)
print(hash(lst))

list_string = line.split(',')


temp_file = open("temp_file.txt", "w")
c = 0
for el in list_string:
    c += hash(el)
    c_temp = str(c) + '\n'
    temp_file.write(c_temp)
    # print(c)
# print(c)
print(hash(list('rn')))
print(hash(list('cm')))


