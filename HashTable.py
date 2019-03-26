#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""Simple Hash Table Implementation

Landscape Rebate Program Qualifying Plant List for Santa Clara Valley Water District:
(https://scvwd.dropletportal.com/public/pdf/plant_list/full/)
    - Just highly efficient lookup by index number in the list
"""

from pandas import DataFrame, read_csv
import pandas as pd

HASH_TABLE_SIZE = 100

class Pair(object):
    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable(object):
    def __init__(self, size):
        self._size = size
        self._array = [None] * size

    def _hash(self, key):
        # TODO: hash function
        hash = key

        return hash

    def get(self, key):
        valuePair = None

        hash = self._hash(key)
        head = self._array[hash % self._size]

        while head:
            if head.value.key == key:
                valuePair = head.value
                break
            
            head = head.next

        return valuePair

    def add(self, pair):
        hash = self._hash(pair.key)
        index = hash % self._size

        newHead = ListNode(pair)

        if self._array[index]:
            newHead.next = self._array[index]

        self._array[index] = newHead
    
    def __str__(self):
        """Print only 3 first array lists.
        """
        index = 0
        resultString = list()

        for item in self._array:
            if item:
                node = item

                indexString = list()
                indexString.append('[i = {}] : '.format(index))

                while(node):
                    indexString.append('({} = {})'.format(node.value.key, node.value.value))

                    node = node.next
                
                index += 1

                resultString.append(''.join(indexString))

                # Print only 5 first array lists
                if index >= 3:
                    break

        return '\n\n'.join(resultString)

        
# Read the file with Plants List
file = r'SCVWD_Qualified_Plants.csv'

df = pd.read_csv(file)

# Let's build a hash table with all the scientific names of plants
hashTable = HashTable(HASH_TABLE_SIZE)

index = 0
for item in df['Scientific_Name']:
    pair = Pair(index, item)
    hashTable.add(pair)
    index += 1

# Print first 2 linked lists in the hash table
print(hashTable)

# Test
print('Let\'s lookup some values')
print('Plant number 5 is {}'.format(hashTable.get(5).value))
print('Plant number 123 is {}'.format(hashTable.get(123).value))
print('Plant number 450 is {}'.format(hashTable.get(450).value))