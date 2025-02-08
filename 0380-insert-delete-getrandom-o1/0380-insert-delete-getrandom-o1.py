from random import randint

class RandomizedSet:

    def __init__(self):
        self.dictionary = {}
        self.elements_list = []

    def insert(self, val: int) -> bool:
        if val not in self.dictionary:
            self.elements_list.append(val)
            self.dictionary[val] = len(self.elements_list)-1
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.dictionary:
            ind_val =  self.dictionary[val]
            self.dictionary[self.elements_list[-1]] = ind_val 
            self.elements_list[ind_val],self.elements_list[-1] = self.elements_list[-1],self.elements_list[ind_val]
            self.elements_list.pop()
            del self.dictionary[val]
            return True
        return False

    def getRandom(self) -> int:
        rand = randint(0,len(self.elements_list)-1)
        return self.elements_list[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()