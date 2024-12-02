input = "input/1202.txt"

TEST = [[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]]

def parse_file_to_intlists(f):

    d = []
    
    for line in f:
        l = line.split(" ")
        l[-1].strip("\n")
        int_list = list(map(lambda x: int(x), l))
        d.append(int_list)
    return(d)


def is_safe(l, curr):
    print("checking", l)

    def is_valid(a, b):
        if abs(b - a) >= 1 and abs(b - a) <= 3:
            return True
        else:
            return False

    if len(l) == 1:
        return True
    else:
        prev = curr
        j = l[0]
        k = l[1]
        if prev <= j and j < k and is_valid(j, k):
            return is_safe(l[1:], j)
        elif prev >= j and j > k and is_valid(j, k):
            return is_safe(l[1:], j)
        else:
            return False


def count_safe_reports(lists):

    total = 0
    
    for l in lists:
        if is_safe(l, l[0]):
            total += 1

    return total


with open(input, "r") as f:
    reports = parse_file_to_intlists(f)
    print(count_safe_reports(reports))


# print(count_safe_reports(TEST))

# print(is_safe([7, 6, 4, 2, 1], 7))
# print(is_safe([1, 2, 7, 8, 9], 1))
# print(is_safe([9, 7, 6, 2, 1], 9))
# print(is_safe([1, 3, 2, 4, 5], 1))
# print(is_safe([8, 6, 4, 4, 1], 8))
# print(is_safe([1, 3, 6, 7, 9], 1))