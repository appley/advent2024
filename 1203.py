import re

input = "input/1203.txt"

TEST = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

PATTERN = "mul\((\d+),(\d+)\)"


def find_int_pairs(s):

    int_list = []
    r = re.findall(PATTERN, s)
    print(r)

    for i in r:
        int_list.append((int(i[0]), int(i[1])))
    
    return int_list


def produce_mul_instructions(int_pairs):

    total = 0

    for i in int_pairs:
        
        total += i[0]*i[1]
    
    return total


def parse_file_and_produce_instructions(f):

    int_pairs = []

    for line in f:

        int_pairs.extend(find_int_pairs(line))
    
    return produce_mul_instructions(int_pairs)




# print(produce_mul_instructions(find_int_pairs(TEST)))

with open (input, "r") as f:
    print(parse_file_and_produce_instructions(f))

    