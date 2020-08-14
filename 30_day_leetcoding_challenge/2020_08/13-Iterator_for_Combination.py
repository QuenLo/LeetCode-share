class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.all = itertools.combinations( characters, combinationLength )
        self.last = characters[-combinationLength:]
        self.res = ""
        

    def next(self) -> str:
        self.res = "".join(next(self.all))
        return self.res

    def hasNext(self) -> bool:
        return self.res != self.last
