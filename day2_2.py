file = open("day2.txt", "r")
lines = file.readlines()

def list_lines(line):
    string = line[8:]
    string = string.split(";")
    res =[]
    for game in string:
        cubes = game.split(",")
        res.append(cubes)
    list_of_list = [[sub_el.split(",") for sub_el in sub_list] for sub_list in res]
    whitespace_list_strip = [[[el.strip() for el in sub_sub_list] for sub_sub_list in sub_list] for sub_list in list_of_list]
    list_list_strip = [[[el.split() for el in sub_sub_list] for sub_sub_list in sub_list] for sub_list in whitespace_list_strip]
    for el in list_list_strip:
        for sub_el in el:
            for sub_sub_el in sub_el:
                sub_sub_el[0] = int(sub_sub_el[0])
    return list_list_strip
### fonctionne bien justqu'à la ligne 100, donc il faudra compter à la main la ligne 100 ####
def id(line):
    string = line[:8]
    string = string.replace(":", "")
    string = string.split(" ")
    # print(string[1])
    string[1] = int(string[1])
    id = string[1]
    return id

test_line = "Game 18: 7 red, 14 blue, 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
# print(list_lines(test_line))

def recup_max(mod_line):
    max_red = 0
    max_blue = 0
    max_green = 0
    for game in mod_line:
        for el in game:
            for sub_el in el:
                if sub_el[1] == 'red' and sub_el[0] > max_red:
                    max_red = sub_el[0]
                if sub_el[1] == 'blue' and sub_el[0] > max_blue:
                    max_blue = sub_el[0]
                if sub_el[1] == 'green':
                    if sub_el[0] > max_green:
                        max_green = sub_el[0] 
                    # print(sub_el[0])
    number = max_red * max_blue * max_green
    return number

def main():
    sum = 0
    for line in lines[:99]:
        mod_line = list_lines(line)
        temp_number = recup_max(mod_line)
        sum += temp_number
    return sum

# test_mod_line = [[[[7, 'red']], [[14, 'blue']]], [[[2, 'blue']], [[3, 'red']], [[3, 'green']]], [[[4, 'green']], [[12, 'blue']], [[15, 'red']]], [[[3, 'green']], [[12, 'blue']], [[3, 'red']]], [[[11, 'red']], [[2, 'green']]]]
test_mod_line = [[[[7, 'green']], [[14, 'blue']]], [[[2, 'blue']], [[3, 'red']], [[3, 'green']]], [[[4, 'green']], [[12, 'blue']], [[15, 'red']]], [[[3, 'green']], [[12, 'blue']], [[3, 'red']]], [[[11, 'red']], [[2, 'green']]]]

test2_mod_line = [[[[9, 'blue']], [[12, 'red']]], [[[9, 'blue']], [[11, 'red']], [[13, 'green']]], [[[9, 'blue']], [[1, 'red']], [[13, 'green']]], [[[4, 'blue']], [[12, 'green']]], [[[10, 'blue']], [[17, 'red']], [[8, 'green']]]]
# print(test2_mod_line)
print(main())
# print(recup_max(test_mod_line))
# print(recup_max(test2_mod_line))
