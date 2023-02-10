def dividers(x:int):
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            yield i
    yield x

def div(x:int):
    num_list =[]
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            num_list.append(i)
    num_list.append(x)
    return num_list


if __name__ == '__main__':
    #for i in dividers(6):
        #print(i)
    print(div(6))