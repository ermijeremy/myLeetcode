class ProductOfNumbers:

    def __init__(self):
        self.element = []

    def add(self, num: int) -> None:
        self.element.append(num)

    def getProduct(self, k: int) -> int:
        self.last_k = self.element[len(self.element)-k:]
        return prod(self.last_k)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)