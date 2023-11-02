from collections import Counter

file = "inputs/day08_test.txt"

# 1, 4, 7, 8
unique_lengths = [2, 4, 3, 7]
unique_keys = ["cf", "bcdf", "acf", "abcdefg"]
numbers = []
sorted_numbers = []
unique_selection = []

with open(file) as f:
    for line in f:
        split_line = line.split('|')
        numbers = split_line[1].strip().split(' ')
        for number in numbers:
            sorted_numbers.append("".join(sorted(number)))

for unique in sorted_numbers:
    if len(unique) in unique_lengths:
        unique_selection.append(unique)
print("Assignment 1: ", len(unique_selection))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def decode(code: list[str]):
    decoded_list = {}
    #print(code)
    code.sort(key = len) 
    #print(code)
    for string in code:
        if len(string) == 2:
            decoded_list[1] = string
        elif len(string) == 4:
            decoded_list[4] = string
        elif len(string) == 3:
            decoded_list[7] = string
        elif len(string) == 7:
            decoded_list[8] = string
        elif len(string) == 5:
            if len(intersection(string, decoded_list[7])) == 3:
                decoded_list[3] = string
            elif len(intersection(string, decoded_list[4])) == 3:
                decoded_list[5] = string
        elif len(string) == 6:
            if len(intersection(string, decoded_list[7])) == 3:
                decoded_list[9] = string
            elif len(intersection(string, decoded_list[8])) == 6:
                decoded_list[0] = string
    print(decoded_list)
    return decoded_list

with open(file) as f:
    for line in f:
        split_line = line.split('|')
        code = split_line[0].strip().split(' ')
        split_code = []
        for string in code:
            split_code.append([string[i] for i in range(0, len(string))])
        #print(code)
        #print(split_code)
        translation = decode(split_code)
        #numbers = split_line[1].strip().split(' ')
        #for number in numbers:
        #    sorted_numbers.append("".join(sorted(number)))



#[]
#lst1 = ['c', 'f']
#lst2 = ['c', 'f', 'b', 'd']
#print(intersection(lst1, lst2))
# Driver Code
##lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
#lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
#print(intersection(lst1, lst2))