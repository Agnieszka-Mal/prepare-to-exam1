import random



def shorten(text):
    result = []
    for word in text.split():
        result.append(word[0])
    return "".join(result).upper()



def name_sorter(name):
    names = {
        "female": [],
        "male": [],
    }

    for word in name:
        if word[-1] == 'a':
            names["female"].append(word)
        elif word[-1] != 'a':
            names["male"].append(word)
    return names

def check_palindrome(text):
    #k = text.split()
   # x = "".join(k).lower()
    y = [i for i in text.lower() if i.isalpha()]
    l = y[::-1]
    return l == y


def div(start:int, stop:int):
    num_list = [i for i in range(start, stop + 1) if i % 2 == 0 and i % 3 != 0 ]
    return num_list

def roll(trow, dice, modifier):
    dices = [3, 4, 6, 8, 10, 12, 100]
    if dice not in dices:
        raise Exception ("No such dice!")
    else:
        return sum(random.randint(1, dice) for _ in range(trow)) + modifier


if __name__ == "__main__":
    #print(shorten("Don't repeat yourself"))
    #print(shorten("All terrain armoured transport"))
    #print(name_sorter(["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]))
    print(check_palindrome("Kobyła, ?ma mały! bok"))
    #print(check_palindrome("Kobyła na sankach"))
    #print(div(0, 20))
    #print(roll(2, 10, 20))
