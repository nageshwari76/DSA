class Fancy:
    def __init__(self):
        self.MOD = 10**9 + 7
        # To store base values such that we can later apply transforms
        self.vals = []
        # Overall transformation variables
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        # Reverse existing transformations so we can store a normalized base
        norm = (val - self.add) % self.MOD
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)  # modular inverse
        self.vals.append((norm * inv_mul) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        # Apply all transformations
        return (self.vals[idx] * self.mul + self.add) % self.MOD