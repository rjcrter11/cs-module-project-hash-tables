class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.keys = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.keys / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_val = 5381
        for c in key:
            hash_val = (hash_val * 33) + ord(c)
        return hash_val

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # self.storage[slot] = value

        # Check hash value
        # If nothing is at that slot, key value goes there
        # If it finds a key that matches passed in node's key, overwrite existing with new value
        # Change pointers -- node = node.next, curr = node
        # Else, create new entry in LL
        # Add one to the key count
        # Otherwise, create a new hash table and store at the head
        # Add one to the key count
        # Do logic for load_factor doubling
        # if more than 0.7, el. count = 0, self.capacity * 2

        slot = self.hash_index(key)
        node = self.storage[slot]
        if node is not None:
            while node is not None:
                if node.key == key:
                    node.value = value
                curr = node
                node = node.next
            curr.next = HashTableEntry(key, value)
            self.keys += 1

        else:
            self.storage[slot] = HashTableEntry(key, value)
            self.keys += 1

        if self.get_load_factor() >= 0.7:
            self.keys = 0
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # slot = self.hash_index(key)
        # if self.storage[slot] is None:
        #     print('Key not found')
        # self.put(key, None)

        # find hash value
        # node is the value at that storage index
        # Check if there's nothing at specified index
        # Assign pointers for node keys
        # Do logic for reducing table size

        slot = self.hash_index(key)
        current = self.storage[slot]

        if current is None:
            print('Key not found')
        elif current.next is None:
            self.storage[slot] = None
            self.keys -= 1

        else:
            prev = None
            while current.key != key and current.next is not None:
                prev = current
                current = current.next

            if current.next is None:
                prev.next = None
                self.keys -= 1

            else:
                current = current.next
                self.keys -= 1

        if self.get_load_factor() < 0.2:
            new_capacity = self.capacity // 2

            if new_capacity < MIN_CAPACITY:
                new_capacity = MIN_CAPACITY
            self.resize(new_capacity)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # slot = self.hash_index(key)

        # if self.storage[slot] is None:
        #     return None
        # else:
        #     return self.storage[slot]

        slot = self.hash_index(key)
        node = self.storage[slot]

        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # Store existing hash table values
        # Init new hash table and update references
        # Reinsert nodes w/ put, which will rehash and insert

        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        for node in old_storage:
            while node:
                self.put(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
