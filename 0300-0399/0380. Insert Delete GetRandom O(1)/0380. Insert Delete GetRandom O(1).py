class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # Dictionary for O(1) lookup
        self.values = []  # List for O(1) random access

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        # [...val...last]
        # [...last...last]
        # last换到val的位置， val_to_index的index也应该更新
        # [...last...] pop
        # 因为val已经不存在应该删除原本的index
        # Move the last element to the position of the element to delete
        self.values[index] = self.values[-1]
        self.val_to_index[self.values[-1]] = index
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        self.values[index] = self.values[-1]
        self.val_to_index[self.values[-1]] = index
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.values)