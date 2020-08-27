#This file contains the code to implement the hash table,
# hash table selected based on requirements and ease of use
class ChainingHashTable:
    # function that initializes and defines the variables key and item
    # Space-time complexity O(1)
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    #gets the bucket for each cell in the hash table
    # Space-time complexity O(1)
    def getBucket(self, key):
        bucket = int(key) % len(self.table)
        return bucket
    #used to insert new values
    # Space-time complexity O(N)
    def insert(self, key, value):
        itemKey = self.getBucket(key)
        itemValue = [key, value]

        if self.table[itemKey] is None:
            self.table[itemKey] = list([itemValue])
            return True
        else:
            for item in self.table[itemKey]:
                if item[0] == key:
                    item[1] = itemValue
                    return True
            self.table[itemKey].append(itemValue)
            return True
    #updates existing data and over writes it
    # Space-time complexity O(N)
    def update(self, key, value):
        itemKey = self.getBucket(key)
        if self.table[itemKey] is not None:
            for item in self.table[itemKey]:
                if item[0] == key:
                    item[1] = value
                    print(item[1])
                    return True
    # searches the table usesing the key and gets the item specified
    # Space-time complexity O(N)
    def search(self, key):
        itemKey = self.getBucket(key)
        if self.table[itemKey] is not None:
            for item in self.table[itemKey]:
                if item[0] == key:
                    return item[1]
        return None
    #deletes a value
    # Space-time complexity O(N)
    def remove(self, key):
        itemKey = self.getBucket(key)

        if self.table[itemKey] is None:
            return False
        for i in range(0, len(self.table[itemKey])):
            if self.table[itemKey][i][0] == key:
                self.table[itemKey].pop(i)
                return True
        return False