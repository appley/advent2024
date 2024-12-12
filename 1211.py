TEST = "0 1 10 99 999"
TEST2 = "125 17"

INPUT = "5 89749 6061 43 867 1965860 0 206250"

def process_zero(e):  
    return str(1)


def process_even_count(e):

    def process_leading_zero(e):
        s = ""
        if int(e[0]) != 0:
            return e
        if len(e) == 1:
            return e
        else:
            return process_leading_zero(e[1:])

    return [
        process_leading_zero(
            e[:int(len(e)/2)]), 
        process_leading_zero(
            e[int(len(e)/2):])]


def process_other(e):
    return [str(int(e)*2024)]


def process_stone(stone):

    if int(stone) == 0:
        return process_zero(stone)
    elif len(stone) % 2 == 0:
        return process_even_count(stone)
    return process_other(stone)


def blink(stones_list):

    l = []

    for stone in stones_list:
        l += process_stone(stone)

    return(l)


def process_blinks(stones_list, num_blinks):

    count = 0
    if count == num_blinks:
        return stones_list
    else:
        return process_blinks(blink(stones_list), num_blinks-1)

    

x = process_blinks(INPUT.split(), 15)
print(x)
print(len(x))



    

