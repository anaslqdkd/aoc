import re

file = open("day1.txt", "r")
lines = file.readlines()
mutable_lines = lines[:]

dict = { "one": "1",
        "zero": "0",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
}
word_numbers = list(dict.keys())
    
def numbers_from_word(line):
    pattern = r'(?:1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine)'
    matches = []
    start_pos = 0
    
    while True:
        match = re.search(pattern, line[start_pos:])
        if match:
            matches.append(match.group())
            start_pos += match.start() + 1
        else:
            break
    
    return matches
print(numbers_from_word("eightoneight"))

def convert_words(line):
    res = []
    for el in line:
        string = el
        if string in word_numbers:
            mutable_string = string.replace(string, dict[string])
            res.append(mutable_string)
        else:
            res.append(string)
    return res

# def extract_word():
#     res = []
#     for line in mutable_lines:
#         extract_word_numbers = numbers_from_word(line)
#         res.append(extract_word_numbers)
#     return res


def main():
    res = []
    res_res = []
    sum = 0
    for line in lines:
        temp_line = []
        reg_line = numbers_from_word(line) 
        convert_line = convert_words(reg_line)
        res.append(convert_line)
    for el_list in res:
        temp_str = el_list[0] + el_list[-1]
        res_res.append(temp_str)
    number_list = [int(char) for char in res_res]
    for el in number_list:
        sum += el
    return sum



example_line ="eightoneightlfksj4lk3one"
reg_line = numbers_from_word(example_line)
print(reg_line)
# print(reg_line)
# print(convert_words(reg_line))
# print(convert_line)
print(main())
