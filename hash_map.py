# Course: CS261 - Data Structures
# Student Name:  Sarah Welsh
# Assignment: 5
# Description:  Hash map functions


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears all buckets from hash map without changing capacity of dynamic array.
        """
        self.size = 0
        for i in range(0, self.capacity):
            if self.buckets.get_at_index(i).size != 0:
                self.buckets.set_at_index(i, LinkedList())

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key.
        """
        hash_val = self.hash_function(key) % self.capacity
        if self.buckets.get_at_index(hash_val).contains(key):
            return self.buckets.get_at_index(hash_val).contains(key).value

    def put(self, key: str, value: object) -> None:
        """
        If the key is currently associated with a value, replaces that node with a new node associating the key with
        the updated value.  If the key doesn't exist currently, adds a new node with the key and associated value.
        """
        hash_val = self.hash_function(key) % self.capacity
        if self.buckets.get_at_index(hash_val).contains(key):
            self.buckets.get_at_index(hash_val).remove(key)
            self.buckets.get_at_index(hash_val).insert(key, value)

        else:
            self.buckets.get_at_index(hash_val).insert(key, value)
            self.size += 1


    def remove(self, key: str) -> None:
        """
        Removes first node containing the given key.
        """
        hash_val = self.hash_function(key) % self.capacity
        if self.contains_key(key):
            self.buckets.get_at_index(hash_val).remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        If the key exists in the hash map, return True.  If not, return False.
        """
        hash_val = self.hash_function(key) % self.buckets.length()
        if self.buckets.get_at_index(hash_val).contains(key):
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the dynamic array.
        """
        empties = self.capacity
        for i in range(0, self.capacity):
            if self.buckets.get_at_index(i).size != 0:
                empties -= 1
        return empties

    def table_load(self) -> float:
        """
        Calculates and returns the table load.
        """
        entries = 0
        for i in range(0, self.capacity):
            if self.buckets.get_at_index(i).size != 0:
                entries += self.buckets.get_at_index(i).size
        return entries / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes capacity of hash map to a new value and rehashes all existing entries.
        """
        if new_capacity < 1:                # if new capacity is less than one, do nothing.
            return

        # get keys in original list
        keys = self.get_keys()

        # create copy of original hash map
        old_HM = HashMap(self.capacity, self.hash_function)
        for i in range(0, self.buckets.length()):
            old_HM.buckets.set_at_index(i, self.buckets.get_at_index(i))

        # save original capacity value
        old_capacity = self.capacity

        # add or subtract buckets in hash map to match new capacity
        add_capacity = new_capacity - self.capacity
        self.clear()
        if add_capacity > 0:
            while add_capacity > 0:
                self.buckets.append(LinkedList())
                add_capacity -= 1
        elif add_capacity < 0:
            while add_capacity < 0:
                self.buckets.pop()
                add_capacity += 1

        # update size and capacity values
        self.capacity = new_capacity
        self.size = keys.length()

        # rehash keys, putting the value associated with the key into the new location
        for i in range(0, keys.length()):
            old_hash_val = self.hash_function(keys.get_at_index(i)) % old_capacity
            new_hash_val = self.hash_function(keys.get_at_index(i)) % new_capacity
            for entry in old_HM.buckets.get_at_index(old_hash_val):
                if entry.key == keys.get_at_index(i):
                    curr_val = entry.value
            if self.buckets.get_at_index(new_hash_val).contains(keys.get_at_index(i)):
                continue
            else:
                self.buckets.get_at_index(new_hash_val).insert(keys.get_at_index(i), curr_val)


    def get_keys(self) -> DynamicArray:
        """
        Returns a new dynamic array containing all of the keys in the hash map.
        """
        keys = DynamicArray()
        for i in range(0, self.buckets.length()):
            if self.buckets.get_at_index(i).size != 0:
                for entry in self.buckets.get_at_index(i):
                    keys.append(entry.key)

        return keys


# BASIC TESTING
if __name__ == "__main__":
    #
    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.size, m.capacity)
    #
    #
    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)
    #
    #
    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())
    #
    #
    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)
    #
    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)
    #
    #
    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.size, m.capacity)
    # m.resize_table(100)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)

    #
    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    #
    #
    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    #
    #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))
    #

    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)


    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    #
    #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    #
    #
    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')

    #
    # print("\nPDF - resize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    #
    # print("\nPDF - get_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())
    #
    # m.resize_table(1)
    # print(m.get_keys())
    #
    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())
