input = "input/1201.txt"

def parse_file_to_intlists(f):

    a = []
    b = []

    for line in f:
        l = line.split("   ")
        a.append(int(l[0]))
        b.append(int(l[1].strip("\n")))
    
    return(a, b)


def compare_min_vals(lists):

    total = 0
    lista = lists[0]
    listb = lists[1]

    while len(lista) != 0 and len(listb) != 0:
        amin = min(lista)
        bmin = min(listb)

        d = abs(amin - bmin)
        total = total + d
        lista.remove(amin)
        listb.remove(bmin)

    return total


def similarity_scores(lists):

    def check_and_remove(num, list, total):
        if num not in list:
            return total
        else:
            total += 1
            list.remove(num)
            return check_and_remove(num, list, total)
    
    total = 0
    lista = lists[0]
    listb = lists[1]

    for i in lista:
        num_occurences = check_and_remove(
            i, listb, 0)
        if num_occurences != 0:
            score = i * num_occurences
            total += score
    
    return total


# part 1
with open(input, "r") as f:
    lists = parse_file_to_intlists(f)
    print(compare_min_vals(lists))

# part 2
with open(input, "r") as f:
    lists = parse_file_to_intlists(f)
    print(similarity_scores(lists))
