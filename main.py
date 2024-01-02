
countdown=10




def count_down():
    global countdown
    for number in range(10):
        print(countdown)
        countdown = countdown - 1

    return 'hi'

print(count_down())