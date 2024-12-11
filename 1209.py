input = "input/1209.txt"

TEST = "2333133121414131402"


PAIRS = [(2, 0, False), (2, 9, True), (3, 7, True), (2, 4, True), (3, 3, True), (1, 2, True), (3, 1, True), (2, 0, True), (4, 5, False), (4, 6, False), (4, 8, False)]


# 00...111...2...333.44.5555.6666.777.888899

d = {0: 0, 1: 0, 5: 1, 6: 1, 7: 1, 11: 2, 15: 3, 16: 3, 17: 3, 19: 4, 20: 4, 22: 5, 23: 5, 24: 5, 25: 5, 2: 9, 3: 9, 4: 8, 8: 8, 9: 8, 10: 8, 12: 7, 13: 7, 14: 7, 18: 6, 21: 6, 26: 6}


def to_string(f):

    s = ""

    for line in f:
        s += line.strip()
    
    return s


def get_last_index(l):

    if len(l) % 2 == 0:
        return 0
    return 1
    

def compact_by_index(input):

    # produce list of nums to insert in reverse
    nums_list = []
    for i, j in enumerate(input):
        if i%2 == 0:
            nums_list.append(int(j))

    print("nums list", nums_list)

    l = []
    curr_last_index = len(nums_list) - 1

    nums_index = 0

    for i, j in enumerate(input):
        int_j = int(j)
        if i%2 == 0:
            l.append((int_j, nums_index, False))
            nums_index += 1
        else:
            while curr_last_index >= 0:
                curr_last_val = nums_list[curr_last_index]
                print("checking index: ", curr_last_index, "item: ", curr_last_val)
                if curr_last_val <= int_j:
                    l.append((curr_last_val, curr_last_index, True))
                    curr_last_index -= 1
                else:
                    curr_last_index -= 1
            # l.append((int_j, False))
    
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
                # spaces.append(curr_index)
                curr_index += 1
        
        new_list_index += int(j)

    return (nums, spaces)


def to_list_two(input):

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

        num_times_loop = int(j[0])

        if i%2 == 0 or j[1] is True:
            nums.update(to_index_pairs(num_times_loop, new_list_index, num_index))
            # print("nums", nums)
            num_index += 1

        else:
            curr_index = new_list_index
            for k in range(num_times_loop):
            #     spaces.append(curr_index)
                curr_index += 1
        
        new_list_index += int(j[0])

    return sorted(nums.items())



def to_compact_dict(t):

    d = t[0]
    
    for i in t[1]:
        if i < len(d):
            max_d = max(d)
            d[i] = d[max_d]
            d.pop(max_d)
    
    return sorted(d.items())
    

def check_sum(d):

    total = 0

    for i in d:
        total += i[0] * i[1]

    return total
        

# print(check_sum(to_compact_dict(to_lists(TEST))))

    

# print(to_compact_dict(to_lists(TEST)))

# with open(input, "r") as f:

#     print(check_sum(to_compact_dict(to_lists(to_string(f)))))


# with open(input, "r") as f:

# print(compact_by_index(TEST))
print(to_list_two(PAIRS))




    








