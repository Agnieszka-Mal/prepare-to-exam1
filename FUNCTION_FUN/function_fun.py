def find_boun(lista):
    new_lista = [i for i in lista if (type(i) == int or type(i) == float)]
    if lista == []:
        return None
    else:
        return min(new_lista), max(new_lista)

#print(find_boun([]))

def censor(t):
    x = ['Java', 'C#', 'Ruby', 'PHP']
    words = t.split()
    n = len(words)
    for i in range(n):
        if words[i] in x:
            words[i] = '****'
    new_t = ' '.join(words)
    return new_t

import random
def rnd(n):
    return sum(random.randint(1, 100) for i in range(n)) / n

print(rnd(5))



