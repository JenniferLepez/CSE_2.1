my_num = 15
secret_num = 25

def number_eal():
    if my_num > secret_num:
        print("your number is too large")
    elif my_num < secret_num:
        print("your number is too small")
    else:
        print("your number matches")

    my_num = input