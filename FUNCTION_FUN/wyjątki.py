def safe_get(l, index: int):
    try:
        return l[index]
    except IndexError:
        return None


l = [1, 'kot', 'fuu']
print(safe_get(l, 8))

def phone(number):
    lista_number = [518516052, 517177587, 695855600, 695855610]
    try:
        if number in lista_number:
            return number
        else:
            raise Exception("Nie ma takiego numeru!")

    except Exception as e:
            return e
