import random

def randNumGen(size):
    # This function generate number
    start_range = 10**(size-1)
    end_range = (10**size)-1
    return random.randint(start_range, end_range)


def reverseNum(num,revr_num):
    #This function reverse a number using recursive method
    if num ==0:
        return revr_num
    else:
        Reminder = num % 10
        revr_num = (revr_num * 10) + Reminder
    return  reverseNum(num // 10,revr_num)
