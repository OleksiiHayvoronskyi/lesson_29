# Завдання 1. Написати клас для створення і роботи з хеш-таблицями.
# Клас повинен містити такі функції:
# створення хеш-таблиці;
# пошук, додавання і видалення нових елементів;
# друк хеш-таблиці;
# виправлення колізій.

print('--- Task 1 ---')


# Initialisation class.
class HashTable:
    def __init__(self):
        self.data = None
        self.size = 12  # Size of a hash table.
        self.slots = [None] * self.size  # Keys.
        self.elements = [None] * self.size  # Elements.

    # Insert data and solving collision.
    def insert(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        print(f'Key [{key}] = element "{data}",  position:', hash_value)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.elements[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.elements[hash_value] = data  # replace.
            # Solving collision with linear algorithm.
            else:
                print('\nWarning!')
                print(f"Collision has occurred for element '{data}' "
                      f"with key [{key}] at the position {hash_value}.")
                next_slot = self.rehash(hash_value, len(self.slots))
                # Findind a new position.
                print(f'Element "{data}" has been replaced to the position '
                      f'{next_slot}. \n')
                while self.slots[next_slot] is not None and \
                        self.slots[next_slot] != key:
                    nnext_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.elements[next_slot] = data
                else:
                    self.elements[next_slot] = data  # replace

    # Method to return position for a given element.
    def hash_function(self, key, size):
        return key % size

    # Replace data at a new position.
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get_element(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.elements[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def delete(self, key):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] == key:  # Item in original slot
            self.slots[hash_value] = None
            self.data[hash_value] = None
        else:
            # if key not found in original slot, do a search for it
            next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] is not key:
                next_slot = self.rehash(hash_value, len(self.slots))
                if self.slots[next_slot] == key:
                    self.slots[next_slot] = None
                    self.data[next_slot] = None
                else:
                    self.slots[next_slot] = None

    def __delitem__(self, key):
        return self.delete(key)

    def __getitem__(self, key):
        return self.get_element(key)

    def __setitem__(self, key, data):
        self.insert(key, data)


ht = HashTable()
print('Inserted data:')
ht[54] = 'Kyiv'
ht[45] = 'Praga'
ht[64] = 'Berlin'
ht[50] = 'Krakov'
ht[30] = 'Paris'
ht[14] = 'Madrid'

print('Keys of the table:', ht.slots)
print('Elements of the table:', ht.elements)
print('Quantity of table:', len(ht.slots), 'slots.')
