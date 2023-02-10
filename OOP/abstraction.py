def middle_elements(sequences):
    new_list = []
    for element in sequences:
        if len(element) != 0:
            new_list.append(element[len(element) // 2])
        else:
            continue
    return new_list

#print(middle_elements([[1, 2, 3, 4, 8, 7], [1, 2, 3], [], ['kot', 'pies', 'mysz']]))

from math import ceil
class SequenceOfNumbers:

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def generation_list(self):
        new_list = [i for i in range(self.start, self.stop, self.step)]
        return new_list

    def __len__(self):
        self.list_lenght = ceil((self.stop - self.start) / self.step)
        return self.list_lenght

    def __getitem__(self, index: int):
        try:
            return [i for i in range(self.start, self.stop, self.step)][index]
        except IndexError:
            return "Index out of range!!!"



x = SequenceOfNumbers(1, 10, 2)
print(x.generation_list())
print(len(x))
print(x[7])
