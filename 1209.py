input = "input/1209.txt"

TEST = "2333133121414131402"

d = {0: 0, 1: 0, 5: 1, 6: 1, 7: 1, 11: 2, 15: 3, 16: 3, 17: 3, 19: 4, 20: 4, 22: 5, 23: 5, 24: 5, 25: 5, 2: 9, 3: 9, 4: 8, 8: 8, 9: 8, 10: 8, 12: 7, 13: 7, 14: 7, 18: 6, 21: 6, 26: 6}


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
        d = {}
        for i in range(num_times_loop):
            d[start_index] = curr_num
            start_index +=1

        # print("returning", l)
        return d

    nums = {}
    spaces = []
    new_list_index = 0
    num_index = 0

    # (index, num)
    #nums [(0, 0), (1, 0), (5, 1), (6, 1), (7, 1)]
    for i, j in enumerate(input):

        num_times_loop = int(j)

        if i%2 == 0:
            nums.update(to_index_pairs(num_times_loop, new_list_index, num_index))
            # print("nums", nums)
            num_index += 1

        else:
            curr_index = new_list_index
            for k in range(num_times_loop):
                spaces.append(curr_index)
                curr_index += 1
        
        new_list_index += int(j)

    return (nums, spaces)


def to_compact_dict(t):

    d = t[0]
    
    for i in t[1]:
        max_d = max(d)
        d[i] = d[max_d]
        d.pop(max_d)
    
    return sorted(d.items())
    

def check_sum(d):

    total = 0

    for i in d:
        total += i * d[i]

    return total
        

# print(check_sum(to_compact_dict(to_lists(TEST))))

    

print(to_compact_dict(to_lists(TEST)))

# with open(input, "r") as f:



    # print(to_disk_map(to_string(f)))

    # print(check_sum(smoosh(to_disk_map(TEST))))

    # print(check_sum(smoosh(to_disk_map(to_string(f)))))


    








