file = open("day1.txt", "r")
lines = file.readlines()
mutable_lines = lines[:]

number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def line_to_numbers(line):
    res = ""
    for char in line:
        if char in number_list:
            res += char
    return res

def recup_numbers():
    res = []
    for line in mutable_lines:
        mutable_line = line[:]
        number_line = line_to_numbers(mutable_line)
        res.append(number_line)
    return res


def pair_line_function(string_line):
    res = []
    for el in string_line:
        first_el = el[0]
        last_el = el[-1]
        string = first_el + last_el
        res.append(string)
        
    return res

def main():
    string_line = recup_numbers()
    pairs_line =pair_line_function(string_line)
    convert_line = [int(el) for el in pairs_line]
    sum = 0
    for num in convert_line:
        sum += num
    return sum

file.close()
##############
test_line = "1lfks2dsdlsfk3" 
# print(recup_numbers())
string_line = recup_numbers()
# print(main(string_line))
# pairs_line = main(string_line)
# convert_line = [int(el) for el in pairs_line ]
print(main())
