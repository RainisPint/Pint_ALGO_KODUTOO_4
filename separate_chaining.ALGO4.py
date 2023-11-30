class Node:                                 # defineerime klassi Node, mis esindab üksikut elementi linklistis
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  

class SeparateChainingHashTable:            
    def __init__(self, size):
        self.size = size  
        self.table = [None] * size  

    def hash_function(self, key):   # võtme jagamine tabeli suurusega
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)  # leian indeksi räsiväärtuse abil

        if self.table[index] is None:               # kui räsiväärtusele pole veel midagi lisatud, loome uue linklisti
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]              # kui räsiväärtusel on juba linklist olemas, lisame uue elemendi selle lõppu
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)  # leian indeksi räsiväärtuse abil

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value  # tagastame väärtuse, kui võti leiti
            current = current.next

        
        return None             #kui elementi ei leitud

    
    def display_table(self):            #tabel
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")

hash_table = SeparateChainingHashTable(size = 8)

#näitelemendid
hash_table.insert(5, "A")
hash_table.insert(10, "B")
hash_table.insert(15, "C")
hash_table.insert(20, "D")
hash_table.insert(30, "E")
hash_table.insert(50, "F")
hash_table.insert(60, "G")


print("Tabel pärast elementide lisamist:")
hash_table.display_table()

#elemndi leidmine
search_key = 20
result = hash_table.search(search_key)

if result is not None:
    print(f"Element võtmega {search_key} leitud: {result}")
else:
    print(f"Elementit võtmega {search_key} ei leitud.")

