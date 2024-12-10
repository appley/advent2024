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


def to_lists(input):

    def to_index_pairs(num_times_loop, start_index, curr_num):
        l = []
        for i in range(num_times_loop):
            l.append((start_index, curr_num))
            start_index +=1

        # print("returning", l)
        return l

    nums = []
    spaces = []
    new_list_index = 0
    num_index = 0

    # (index, num)
    #nums [(0, 0), (1, 0), (5, 1), (6, 1), (7, 1)]
    for i, j in enumerate(input):

        num_times_loop = int(j)

        if i%2 == 0:
            nums += to_index_pairs(num_times_loop, new_list_index, num_index)
            print("nums", nums)
            num_index += 1

        else:
            curr_index = new_list_index
            for k in range(num_times_loop):
                spaces.append(curr_index)
                curr_index += 1
        
        new_list_index += int(j)

    return (nums, spaces)


def to_compact(t):
    
    l = []
    count = 0
    
    for i in t[0]:
        

        

    

def smoosh(l):

    print(len(l))
    def move_last(index, curr_s):
        return curr_s[:index] + [curr_s[-1]] + curr_s[index+1:len(curr_s)-1]
    
    # if "." not in l:
    #     return l
    
    # else:
        print(l)

    new_l = l.copy()
    for i, j in enumerate(l):
        print(l)
        print("pass: ", i, j, len(new_l))
        if "." not in l:
            return l
        else:
        
        # print(i, l)
        # print("current string: ", l)
            if j == ".":
                l[i] = l[-1]
                l.pop()
        

            # new_s = move_last(i, l)
            # print(i, l, new_s)

    print(l)
    return l
                # return smoosh(l)

            

def check_sum(s):

    total = 0

    for i, j in enumerate(s):
        total += i * int(j)

    return total
        

print(to_lists(TEST))
    
# with open(input, "r") as f:



    # print(to_disk_map(to_string(f)))

    # print(check_sum(smoosh(to_disk_map(TEST))))

    # print(check_sum(smoosh(to_disk_map(to_string(f)))))


    








