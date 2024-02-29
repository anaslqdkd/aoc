import re

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

list_line = line.split(',')
# print(list_line)

def recup_word(string):
    mot = ''
    n = len(string)
    i = 0
    while i!=n:
        if string[i] == '-' or string[i] == '=':
            break
        else:
            mot += string[i]
        i += 1
    return mot

def recup_symbol(string):
    pattern = r'(=|-)'
    match = re.search(pattern, string)
    return match.group()

def recup_number(string):
    pattern =r'(\d)'
    match = re.search(pattern, string)
    if match:
        return match.group()
    else:
        return None

word_list = []

for el in list_line:
    word = recup_word(el)
    if word not in word_list:
        word_list.append(word)

# print(word_list)

number_list = []

for el in word_list:
    number = hash(el)
    if number not in number_list:
        number_list.append(number)
    number_list.append(3)
number_list.sort()
# print(number_list)

# print(recup_number('rd=5'))
di = {key: [] for key in number_list} 
# print(dict[0])
# print(dict)
def get_list_word(di, box):
    if box not in di.keys():
        return "Error"
    line = di[box]
    res = []
    for el in line:
        res.append(el[0])
    return res

def get_index_word(string, di, box):
    lst = di[box]
    for i in range(len(lst)):
        if lst[i][0] == string:
            return i
    return None 

def place_el(string, di):
    mot = recup_word(string)
    box = hash(mot) 
    symbol = recup_symbol(string)
    number = recup_number(string)
    box_dict = di[box]
    # print(box_dict)
    if symbol == '-':
        if mot in get_list_word(di, box): 
            # print(get_list_word(di, box))
            index = get_index_word(mot, di, box)
            del box_dict[index]
    if symbol == '=':
        if mot in get_list_word(di, box):
            index = get_index_word(mot, di, box)
            box_dict[index][1] = number
        else:
            temp_list = [mot, number]
            box_dict.append(temp_list)
    return di
# print(place_el("rn=3", di))

test_string = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
test_string_list = test_string.split(',')
dict_test = {key: [] for key in number_list}
for el in test_string_list:
    place_el(el, dict_test)
# print(dict_test)
# test_dict = {'0': [['rn', 3], ['cm', 4]]}

# print(get_list_word(test_dict, '0'))
# print(test_dict.keys())
# print(list_line)
def count(di, box):
    lst = di[box]
    number = 0
    for i in range(len(lst)):
        temp_number = (int(box)+1)*(i+1)*int(lst[i][1])
        number += temp_number
    return number


# print(dict_test)
# print(count(dict_test, 0))        


def main():
    f_dict = {key: [] for key in number_list}
    count_value = 0
    for el in list_line:
        place_el(el, f_dict)
    for key in f_dict.keys():
        count_value += count(f_dict, key)

        
    return count_value

print(main())


    



