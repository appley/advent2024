input = "input/1209.txt"

TEST = "2333133121414131402"


def to_string(f):

    s = ""

    for line in f:
        s += line.strip()
    
    return s


def available_space(num, space):

    if num > space:
        return False
    else:
        return True
    

def check_for_space(num, num_id, spaces):

    new_spaces = spaces.copy()
    moved = False
    
    for i, j in enumerate(spaces[:num_id+1]):
        if available_space(num, j):
            new_space = new_spaces[i] - num
            new_spaces.pop(i)
            new_spaces.insert(i, new_space)
            moved = True
            return (moved, i, new_spaces)
    
    return (moved, i, new_spaces)


def to_lists_two(input):

    original = []
    nums_list = []
    spaces_list = []

    for i, j in enumerate(input):

        if i%2 == 0:
            nums_list.append(int(j))
        else:
            spaces_list.append(int(j))
        
        original.append(int(j))

    return (nums_list, spaces_list, original)


def compact_by_index(input):

    def to_index_pairs(num_times_loop, start_index, curr_num):
        d = {}
        for i in range(num_times_loop):
            d[start_index] = curr_num
            start_index +=1

        return d
    
    def find_start(index, d):

        add_count = 0

        if not d.get(index):
            return index
        else:
            while d.get(index + add_count):
                add_count += 1
        return index + add_count
    
    def process_nums(nums, input):
        d = {}
        for i, j in enumerate(nums):
            d.update(to_index_pairs(j, sum(input[:int(i*2)]), i))
        return d

    items = to_lists_two(input)
    nums = items[0]
    spaces = items[1]
    original =  items[2]

    curr_last_num_id = len(nums) - 1

    nums_dict = process_nums(nums, original)
    moved_nums = {}

    while curr_last_num_id >= 1:

        num = nums[curr_last_num_id]

        move = check_for_space(
            num, curr_last_num_id, spaces)

        if move[0] is True:
            start_index = find_start(sum(original[:int(move[1]*2 + 1)]), moved_nums)

            d = to_index_pairs(num, start_index, curr_last_num_id)
            moved_nums.update(d)
            spaces = move[2]
            nums.pop(curr_last_num_id)
            
            curr_last_num_id -= 1
    
        else:
            curr_last_num_id -= 1

    return(nums_dict, moved_nums)


def check_and_remove_moved(dicts):

    values_to_remove = []

    original = dicts[0]
    moved = dicts[1]

    for i in moved:
        values_to_remove.append(moved.get(i))

    filtered_original = {k: v for k, v in original.items() if v not in values_to_remove}
    filtered_original.update(moved)

    return sorted(filtered_original.items())


def to_lists(input):

    def to_index_pairs(num_times_loop, start_index, curr_num):
        d = {}
        for i in range(num_times_loop):
            d[start_index] = curr_num
            start_index +=1

        return d

    nums = {}
    spaces = []
    new_list_index = 0
    num_index = 0

    for i, j in enumerate(input):

        num_times_loop = int(j)

        if i%2 == 0:
            nums.update(to_index_pairs(num_times_loop, new_list_index, num_index))
            num_index += 1

        else:
            curr_index = new_list_index
            for k in range(num_times_loop):
                # spaces.append(curr_index)
                curr_index += 1
        
        new_list_index += int(j)

    return (nums, spaces)


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



# part 1
with open(input, "r") as f:

    print(check_sum(to_compact_dict(to_lists(to_string(f)))))

# part 2
with open(input, "r") as f:

    print(check_sum(check_and_remove_moved(compact_by_index(to_string(f)))))




    








