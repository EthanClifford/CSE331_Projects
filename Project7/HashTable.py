class HashNode:
    """
    DO NOT EDIT
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None]*capacity


    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True


    def __repr__(self):
        str = ""
        for i in range(len(self.table)):
            str += ", "+str(self.table[i].__repr__())
        print(str)

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value):
        """
        Inserts key(string) and value(string) into the HashTable using a HashNode
        Resolves conflicts using quadratic probing
        If a HashNode with the same key is already present, reassigns the value to the new value
        If the load factor is strictly greater than 0.75, calls grow()
        Does NOT allow insertion of empty string
        :param key:  The key to be inserted
        :param value:  The value to be associated with the kye being inserted
        :return:  None
        """
        if key == "":
            return
        init_key = key
        if isinstance(key, str):
            key = self.hash_function(key)
        indx = self.quadratic_probe(init_key)
        if self.table[indx] is None or self.table[indx] is False:
            self.table[indx] = HashNode(init_key, value)
            self.size += 1
        elif self.table[indx].key == init_key:
            self.table[indx].value = value
        if self.size/self.capacity > .75:
            self.grow()

    def quadratic_probe(self, key):
        """
        Runs the quadratic hashing procedure
        Returns the table index of key if key is in the table
        If key is not found in the table, returns the next available index
        Formula follows that of as i increments:
        bucket = (bucket + i*i) % capacity
        :param key:  The key to be searched for
        :return:  The index if the key is in the table, the next available index otherwise
        """
        if key == "":
            return -1
        init_key = key
        if isinstance(key, str):
            key = self.hash_function(key)
        indx = key % self.capacity
        i = 1
        while 1:
            if self.table[indx] is None or self.table[indx] is False:
                return indx
            elif self.table[indx].key == init_key:
                return indx
            indx = (indx+i*i) % self.capacity
            i += 1

    def find(self, key):
        """
        Takes in a key to search for in the Hash Table
        Returns the node with the given key if found, if not found it returns False
        :param key:  The key to be searched for
        :return:  The node with the given key if it exists in the table, False otherwise
        """
        init_key = key
        if isinstance(key, str):
            key = self.hash_function(key)
        indx = key % self.capacity
        if (self.table[indx] is not None) and (self.table[indx] is not False):
            if self.table[indx].key == init_key:
                return self.table[indx]
        indx = (indx+1) % self.capacity
        while indx != key % self.capacity:
            if (self.table[indx] is not None) and (self.table[indx] is not False):
                if self.table[indx].key == init_key:
                    return self.table[indx]
            indx = (indx+1) % self.capacity
        return False

    def lookup(self, key):
        """
        Takes in a key to search for in the Hash Table
        Returns the value of the node with the given key if found, if not found it returns False
        :param key:  The key to be searched for
        :return:  The value of the node with the given key if it exists in the table, False otherwise
        """
        init_key = key
        if isinstance(key, str):
            key = self.hash_function(key)
        indx = key % self.capacity
        if (self.table[indx] is not None) and (self.table[indx] is not False):
            if self.table[indx].key == init_key:
                return self.table[indx].value
        indx = (indx + 1) % self.capacity
        while indx != key % self.capacity:
            if (self.table[indx] is not None) and (self.table[indx] is not False):
                if self.table[indx].key == init_key:
                    return self.table[indx].value
            indx = (indx + 1) % self.capacity
        return False

    def delete(self, key):
        """
        Takes in a key to delete in the Hash Table
        Deletes by setting node to False
        :param key:  The key to be removed
        :return:  None
        """
        init_key = key
        if isinstance(key, str):
            key = self.hash_function(key)
        indx = key % self.capacity
        if (self.table[indx] is not None) and (self.table[indx] is not False):
            if self.table[indx].key == init_key:
                self.table[indx] = False
                self.size -= 1
                return
        indx = (indx + 1) % self.capacity
        while indx != key % self.capacity:
            if (self.table[indx] is not None) and (self.table[indx] is not False):
                if self.table[indx].key == init_key:
                    self.table[indx] = False
                    self.size -= 1
                    return
            indx = (indx + 1) % self.capacity

    def grow(self):
        """
        Doubles capacity
        Rehashes all items in table
        :return: None
        """
        self.capacity *= 2
        self.rehash()

    def rehash(self):
        """
        Reinserts all of the nodes into the HashTable
        :return: None
        """
        i = 0
        sz = 0
        table_contents = [None]*self.size
        while sz < self.size:
            if self.table[i] is not None and self.table[i] is not False:
                table_contents[sz] = self.table[i]
                sz += 1
            i += 1
        i = 0
        self.table = [None]*self.capacity
        self.size = 0
        while i < len(table_contents):
            self.insert(table_contents[i].key, table_contents[i].value)
            i += 1


def string_difference(string1, string2):
    """
    Takes in two strings, uses hash tables to get the difference of characters from the strings
    Returns a set of the different characters, grouped by character
    :param string1: The first string to perform the comparison on
    :param string2: The second string to perform the comparison on
    :return: A set containing the difference between the two strings
    """
    hash1 = HashTable(len(string1))
    hash2 = HashTable(len(string2))
    if hash1.capacity == 0:
        hash1 = HashTable(1)
    if hash2.capacity == 0:
        hash2 = HashTable(1)
    i = 0
    while i < len(string1):
        found_key = hash1.find(string1[i])
        if found_key is not False:
            hash1.insert(found_key.key, found_key.value + 1)
        else:
            hash1.insert(string1[i], 1)
        i += 1
    i = 0
    while i < len(string2):
        found_key = hash2.find(string2[i])
        if found_key is not False:
            hash2.insert(found_key.key, found_key.value + 1)
        else:
            hash2.insert(string2[i], 1)
        i += 1
    i = 0
    result = set()
    mult = 0
    while i < hash1.capacity:
        if hash1.table[i] is not None and hash1.table[i] is not False:
            found_key = hash2.find(hash1.table[i].key)
            if found_key is not False:
                mult = hash1.table[i].value - found_key.value
                if mult < 0:
                    mult *= -1
                if mult != 0:
                    result.add(hash1.table[i].key*mult)
            else:
                result.add(hash1.table[i].key*hash1.table[i].value)
        i += 1
    i = 0
    while i < hash2.capacity:
        if hash2.table[i] is not None and hash2.table[i] is not False:
            found_key = hash1.find(hash2.table[i].key)
            if found_key is False:
                result.add(hash2.table[i].key*hash2.table[i].value)
        i += 1
    return result

