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


def is_safe(l):
    print("checking", l)

    def is_valid(a, b):
        if a < b and b - a >= 1 and b - a <= 3:
            return True
        elif a > b and a - b >= 1 and a - b <= 3:
            return True
        else:
            return False

    if len(l) == 1:
        return True
    else:
        j = l[0]
        k = l[1]
        if is_valid(j, k):
            return is_safe(l[1:])
        

# def is_safe(l):

#     for i in range(len(l)-1):
#         print(l[i])
#         if l[i] < l[i+1] and l[i+1] - l[i] >= 1 and l[i+1] - l[i] <= 3:
#             return True
#         elif l[i] > l[i+1] and l[i] - l[i+1] >= 1 and l[i] - l[i+1] <= 3:
#             return True
#         else:
#             return False


def count_safe_reports(lists):

    total = 0
    
    for l in lists:
        if is_safe(l):
            total += 1

    return total


# with open(input, "r") as f:
#     reports = parse_file_to_intlists(f)
#     print(count_safe_reports(reports))


# print(count_safe_reports(TEST))

print(is_safe([7, 6, 4, 2, 1]))
print(is_safe([1, 2, 7, 8, 9]))
print(is_safe([9, 7, 6, 2, 1]))
print(is_safe([1, 3, 2, 4, 5]))
print(is_safe([8, 6, 4, 4, 1]))
print(is_safe([1, 3, 6, 7, 9]))