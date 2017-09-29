import random

def get_result():
    list_of_bets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    list_of_1_6 = [1, 2, 3, 4, 5, 6]
    list_of_4_9 = [4, 5, 6, 7, 8, 9]
    list_of_7_12 = [7, 8, 9, 10, 11, 12]
    list_of_odd = [1, 3, 5, 7, 9, 11]
    list_of_even = [2, 4, 6, 8, 10, 12]
    list_of_black = [2, 4, 6, 7, 9, 11]
    list_of_red = [1, 3, 5, 8, 10, 12]
    decision = random.choice(list_of_bets)
    if decision in list_of_1_6:
        win_range = "1-6"
    elif decision in list_of_4_9:
        win_range = "4-9"
    elif decision in list_of_7_12:
        win_range = "7-12"
    if decision in list_of_black:
        color = "black"
    else:
        color = "red"
    if decision in list_of_odd:
        oddity = "ODD"
    else:
        oddity = "EVEN"
    print (decision, flush=True)
    print (win_range, flush=True)
    print (color, flush=True)
    print (oddity, flush=True)
    return decision, win_range, color, oddity
    