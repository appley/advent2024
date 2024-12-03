import re

input = "input/1203.txt"

# test strings
TEST = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

PATTERN = "mul\((\d+),(\d+)\)"
DO = "don't\(\).*?do\(\)"


def find_int_pairs(s):

    int_list = []
    r = re.findall(PATTERN, s)

    for i in r:
        int_list.append((int(i[0]), int(i[1])))
    
    return int_list


def produce_mul_instructions(int_pairs):

    total = 0

    for i in int_pairs:
        
        total += i[0]*i[1]
    
    return total
    

def parse_input_and_produce_instructions(input):

    int_pairs = []

    for i in input:

        int_pairs.extend(find_int_pairs(i))
    
    return produce_mul_instructions(int_pairs)


def stringify_file(f):

    s = ""

    for line in f:
        s += line.strip()

    return s


def split_dos(s):

    return re.split(DO, s)



# part 1
with open (input, "r") as f:
    print(parse_input_and_produce_instructions(f))

#part 2
with open (input, "r") as f:
    print(parse_input_and_produce_instructions(split_dos(stringify_file(f))))