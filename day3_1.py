import re
from itertools import chain

file = open("day3.txt", "r")
lines = file.readlines()

char_list = ['*', '&', '@', '#', '/', '%', '+', '$', '-', '=']

number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
matrix = []
for line in lines:
    row = list(line.strip())
    matrix.append(row)

# print(matrix[:1])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] in number_list:
            matrix[i][j] = int(matrix[i][j])
# print(matrix[:1])

index_list = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if type(matrix[i][j]) == int:
            index_list.append((i,j))

all_numbers = []
for line in lines:
    numbers = re.findall(r'\d+', line)
    all_numbers.append(numbers)
# print(index_list[:5])
# print(all_numbers[:1])
all_numbers_conv = [[int(el) for el in list] for list in all_numbers]
flattened_all_numbers = list(chain(*all_numbers))
# for i in range(len(all_numbers)):
#     l = all_numbers[i]
#     for j in range(len(l)):
#         all_numbers[i][j] = int(all_numbers[i][j])
# print(all_numbers_conv)
# print(all_numbers[:2])
# print(flattened_all_numbers)

count_list = []
for el in flattened_all_numbers:
    count = len(el)
    count_list.append(count)

# print(count_list)

position_index = 0
position_tpl = 0
res = []
while (position_tpl != len(index_list)):
    count = count_list[position_index]
    temp_list = index_list[position_tpl:position_tpl+count]
    temp_list.append(int(flattened_all_numbers[position_index]))
    res.append(temp_list)
    position_index += 1
    position_tpl = position_tpl+count


# print(res)
def satisfy_cond(i,j):
    surrounding_coordinates = [(i-1, j-1), (i-1, j), (i-1, j+1),(i, j-1),(i, j+1),(i+1, j-1), (i+1, j), (i+1, j+1)]
    for k,v in surrounding_coordinates:
        if k in (0, 139) or v in (0, 194):
            continue 
        if matrix[k][v] in char_list:
            return False
    return True

def cond(i, j, count):
    inc = count
    while inc != 0:
        if not satisfy_cond(i, j+inc):
            return False
        inc -= 1
    return True


c = 0
test_list = [[(0, 23), (0, 24), (0, 25), 661], [(0, 51), (0, 52), (0, 53), 485], [(0, 56), (0, 57), (0, 58), 565], [(0, 66), (0, 67), (0, 68), 344], [(0, 76), (0, 77), (0, 78), 325], [(0, 116), (0, 117), (0, 118), 841], [(0, 124), (0, 125), (0, 126), 725], [(1, 5), (1, 6), (1, 7), 609]]
test_test_list = [[(0, 23), (0, 24), (0, 25), 661], [(0, 51), (0, 52), (0, 53), 485], [(0, 56), (0, 57), (0, 58), 565], [(0, 66), (0, 67), (0, 68), 344], [(0, 76), (0, 77), (0, 78), 325], [(0, 116), (0, 117), (0, 118), 841], [(0, 124), (0, 125), (0, 126), 725], [(1, 5), (1, 6), (1, 7), 609], [(1, 10), (1, 11), (1, 12), 131], [(1, 29), (1, 30), (1, 31), 512], [(1, 72), (1, 73), (1, 74), 536], [(1, 90), (1, 91), (1, 92), 462], [(1, 100), (1, 101), 60], [(1, 104), (1, 105), (1, 106), 424], [(2, 1), (2, 2), (2, 3), 316], [(2, 21), (2, 22), 39], [(2, 43), (2, 44), (2, 45), 630], [(2, 52), (2, 53), (2, 54), 377], [(2, 63), (2, 64), (2, 65), 919], [(2, 77), (2, 78), 98]]

elem = []
for el in test_test_list:
    k_i, v = el[0]
    k, v_i = el[len(el)-2]
    count = len(el) - 1
    if k_i != 0 and k_i != 139 and v_i != 194 and v != 0:
        i, j = el[0]
        if cond(i,j, count):
            elem.append(el[len(el)-1])

# print(elem)
# print(cond(1,7, 3))

def surrounding_coordinates(i,j):
    res = [(i-1, j-1), (i-1, j), (i-1, j+1),(i, j-1),(i, j+1),(i+1, j-1), (i+1, j), (i+1, j+1)]
    return res

def accept_number(tpl_line):
    number = tpl_line[len(tpl_line)-1]
    count = len(tpl_line) - 1
    for tpl in tpl_line[:len(tpl_line)-1]:
        i, j = tpl
        # print(tpl, number)
        s_coor = surrounding_coordinates(i,j)
        # print(s_coor)
        for el in s_coor:
            a,b = el
            if 0 <= a < len(matrix) and 0 <= b < len(matrix[0]):
                if matrix[a][b] in char_list:
                    # print(a,b)
                    # print(matrix[a][b])
                    return False
    return True 
# test = [(0, 23), (0, 24), (0, 25), 661]
test = [(1, 5), (1, 6), (1, 7), 609]
test_el = [(1, 72), (1, 73), (1, 74), 536]
test_test_el = [(1, 10), (1, 11), (1, 12)]
# print(accept_number(test_el))
line = [[(1, 5), (1, 6), (1, 7), 609], [(1, 10), (1, 11), (1, 12), 131], [(1, 29), (1, 30), (1, 31), 512], [(1, 72), (1, 73), (1, 74), 536], [(1, 90), (1, 91), (1, 92), 462], [(1, 100), (1, 101), 60], [(1, 104), (1, 105), (1, 106), 424], [(2, 1), (2, 2), (2, 3), 316], [(2, 21), (2, 22), 39], [(2, 43), (2, 44), (2, 45), 630], [(2, 52), (2, 53), (2, 54), 377], [(2, 63), (2, 64), (2, 65), 919], [(2, 77), (2, 78), 98]]
gaga = [(1, 10), (1, 11), (1, 12), 131]
# print(accept_number(gaga))
# print(matrix[2])
# print(matrix[2][13])
# sdlk = [(1, 104), (1, 105), (1, 106), 424]
# print(accept_number(sdlk))
# for el in line:
#     print(accept_number(el))
# c = 0
# for el in res:
#     print(accept_number(el))
#     c+=1
#     print(c)

def main():
    accept_list = []
    s = 0
    for el in res:
        if accept_number(el):
            accept_list.append(el[len(el)-1])
    for number in accept_list:
        s += number
    return s 
f = 0
for el in flattened_all_numbers:
    f +=int(el) 
    
# print(main())
# print(flattened_all_numbers)
# print(f)
gaga_list = main()
print(gaga_list)
print(f)

print(main())
[661, 485, 344, 512, 564, 535, 487, 605, 729, 726, 53, 664, 337, 954, 6, 491, 56, 305, 41, 124, 437, 687, 554, 938, 637, 658, 697, 718, 991, 39, 515, 910, 663, 574, 672, 192, 736, 561, 943, 645, 882, 975, 152, 713, 266, 668, 811, 157, 772, 649, 920, 787, 126, 497, 576, 117, 610, 125, 757, 384, 442, 236, 868, 235, 116, 361, 440, 241, 296, 434, 842, 647, 433, 392, 499, 970, 671, 628, 82, 376, 401, 466, 161, 351, 441, 665, 863, 241, 680, 64, 809, 397, 796, 343, 876, 734, 402, 324, 134, 534, 169, 386, 283, 82, 3, 10, 394, 815, 738, 419, 810, 910, 500, 897, 189, 120, 397, 912, 377, 823, 481, 244, 396, 607, 222, 820, 535, 853, 862, 233, 825, 22, 934, 821, 370, 747, 952, 868, 713]

# resultat = f - main()

