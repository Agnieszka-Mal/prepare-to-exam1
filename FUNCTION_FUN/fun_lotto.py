from random import randint, shuffle

def lotto_num():
    lotto_nums = [i for i in range(1, 49)]
    x = shuffle(lotto_nums)
    return x[:6]
lotto_num()

