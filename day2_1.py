#### 12 red cubes, 13 green cubes, 14 blue cubes

file = open("day2.txt", "r")
lines = file.readlines()


original_string = "Game 1: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
string = original_string[8:]
games = string.split(";")
# print(games)
res = []
for game in games:
    cubes = game.split(",") 
    res.append(cubes)
    # for cube in cubes:
    #     parts = cube.strip().split()
    #     print(parts)
    # res.append(cubes)
list_of_list = [[sub_el.split(",") for sub_el in sub_list] for sub_list in res]
whitespace_list_strip = [[[el.strip() for el in sub_sub_list] for sub_sub_list in sub_list] for sub_list in list_of_list]

# print(list_strip)

# for el in whitespace_list_strip:
#     for el_k in el:
#         for el_m in el_k:
#             # print(el_m)
#             el_m.split()
# test = ['5 red']
# test_list = test[0].split()
# print(whitespace_list_strip)
# print(test_list)
# print(res)
    
list_list_strip = [[[el.split() for el in sub_sub_list] for sub_sub_list in sub_list] for sub_list in whitespace_list_strip]
# int_list = [[[[int(el[0]), el[1:].strip()] for el in sub_sub_list] for sub_sub_list in sub_list] for sub_list in whitespace_list_strip]

# int_list = []
for el in list_list_strip:
    for sub_el in el:
        for sub_sub_el in sub_el:
            sub_sub_el[0] = int(sub_sub_el[0])
# print(list_list_strip)
# print(int_list)

# [[[[7, 'red']], [[1, '4 blue']]], [[[2, 'blue']], [[3, 'red']], [[3, 'green']]], [[[4, 'green']], [[1, '2 blue']], [[1, '5 red']]], [[[3, 'green']], [[1, '2 blue']], [[3, 'red']]], [[[1, '1 red']], [[2, 'green']]]]

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

def satisfy_cond(mod_list):
    for game in mod_list:
        for useless_list in game:
            list_duplicate = useless_list[0]
            if list_duplicate[1] == 'red' and list_duplicate[0] > 12:
                # print(list_duplicate[1], list_duplicate[0])
                return False
            if list_duplicate[1] == 'blue' and list_duplicate[0] > 14:
                return False
            if list_duplicate[1] == 'green' and list_duplicate[0] > 13:
                return False
            # for list in game:
    return True
            #     print(list)





def maiN():
    sum_index = 0
    for line in lines[:99]:
        line_id = id(line)
        modified_line = list_lines(line)
        if satisfy_cond(modified_line):
            sum_index += line_id
            # print(line_id)

    return sum_index
        # for game in modified_line:
        #     for useless_list in game:
        #         for list in uselles_list:


        # print(f"the id is {id}: id")
        # print(modified_line)

test_test_line = "Game 8: 4 red, 3 blue, 8 green; 2 red, 16 green; 2 red, 1 blue"

test_line = "Game 18: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green"
# print(id(test_line))
# print(id(test_test_line))
test_mod_line = [[[[7, 'red']], [[14, 'blue']]], [[[2, 'blue']], [[3, 'red']], [[3, 'green']]], [[[4, 'green']], [[12, 'blue']], [[15, 'red']]], [[[3, 'green']], [[12, 'blue']], [[3, 'red']]], [[[11, 'red']], [[2, 'green']]]]

test2_mod_line = [[[[9, 'blue']], [[12, 'red']]], [[[9, 'blue']], [[11, 'red']], [[13, 'green']]], [[[9, 'blue']], [[1, 'red']], [[13, 'green']]], [[[4, 'blue']], [[12, 'green']]], [[[10, 'blue']], [[17, 'red'
]], [[8, 'green']]]]
# print(satisfy_cond(test2_mod_line))

print(main())

# print(list_lines(test_test_line))
