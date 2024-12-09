input = "input/1209.txt"

TEST = "2333133121414131402"


def to_string(f):

    s = ""

    for line in f:
        s += line.strip()
    
    return s


def to_disk_map(input):

    def loop_string(item, num):
        l = []
        for i in range(num):
            l.append(item)
        return l

    l = []

    t = 0
    for i, j in enumerate(input):
        
        int_j = int(j)
        if i%2 == 0:
            k = loop_string(t, int_j)
            t += 1
        else:
            k = loop_string(".", int_j)
        l += k

    return l


def smoosh(l):
    def move_last(index, curr_s):
        return curr_s[:index] + [curr_s[-1]] + curr_s[index+1:len(curr_s)-1]
    
    if "." not in l:
        return l
    
    else:
        for i, j in enumerate(l):
            print(i)
            print("current string: ", l)
            if j == ".":
                new_s = move_last(i, l)
                print(i, l, new_s)
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

    # print(check_sum(smoosh(to_disk_map(TEST))))

    print(check_sum(smoosh(to_disk_map(to_string(f)))))


    








