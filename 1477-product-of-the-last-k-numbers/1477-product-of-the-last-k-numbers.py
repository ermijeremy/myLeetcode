class ProductOfNumbers:

    def __init__(self):
        self.element = [1]
        self.prod = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prod = 1
            self.element = [1]
        else:
            self.prod *= num
            self.element.append(self.prod)

    def getProduct(self, k: int) -> int:
        if k < len(self.element):
            return self.element[-1]//self.element[len(self.element)-k-1]
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)