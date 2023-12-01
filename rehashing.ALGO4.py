class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * size

    def hash_function1(self, key):
        return hash(key) % self.size

    def hash_function2(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def double_hashing(self, key, i):
        return (self.hash_function1(key) + i * self.hash_function2(key)) % self.size

    def insert(self, key, value):
        i = 0
        index = self.hash_function1(key)

        while self.table[index] is not None:
            index = self.double_hashing(key, i)
            i += 1

        self.table[index] = Node(key, value)

    def get(self, key):
        i = 0
        index = self.hash_function1(key)

        while self.table[index] is not None:
            stored_key, value = self.table[index].key, self.table[index].value
            if stored_key == key:
                return value
            index = self.double_hashing(key, i)
            i += 1

        return None

hash_table = HashTable()

hash_table.insert("x", 5)
hash_table.insert("y", 9)

print(hash_table.get("x"))    
print(hash_table.get("y"))   
