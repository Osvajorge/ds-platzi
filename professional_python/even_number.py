import numbers


class EvenNumbers:

    "Class that implements an iterator of every even number until a max"

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.number
            self.num +=2
            return result
        else:
            raise StopIteration
