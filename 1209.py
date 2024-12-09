input = "input/1209.txt"

TEST = "2333133121414131402"
TEST2 = "00000000.....11111.222.......333333333........44..55555......66......77778888888.........9999999...1010.......111111....1212.13........141414.......151515"


def to_string(f):

    s = ""

    for line in f:
        s += line.strip()
    
    return s


def to_disk_map(input):

    def loop_string(item, num):
        s = ""
        for i in range(num):
            s += item
        return s

    s = ""

    t = 0
    for i, j in enumerate(input):
        
        int_j = int(j)
        if i%2 == 0:
            k = loop_string(str(t), int_j)
            t += 1
        else:
            k = loop_string(".", int_j)
        s += k

    return s


def smoosh(s):
    def move_last(index, curr_s):
        return curr_s[:index] + curr_s[-1] + curr_s[index+1:len(curr_s)-1]
    
    if "." not in s:
        return s
    
    else:
        for i, j in enumerate(s):
            print(i)
            print("current string: ", s)
            if j == ".":
                new_s = move_last(i, s)
                print(i, s, new_s)
                return smoosh(new_s)
            

def check_sum(s):

    total = 0
    print(s)

    for i, j in enumerate(s):
        print(i, j)
        total += i * int(j)

    return total
        
    
with open(input, "r") as f:

    # print(to_disk_map(to_string(f)))

    print(check_sum(smoosh(to_disk_map(to_string(f)))))
    








