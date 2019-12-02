#!/usr/bin/env python3

""" HashTable Module

 In computing, a hash table is a data structure that
 implements an associative array abstract data type, a structure
 that can map keys to values. A hash table uses a hash
 function to compute an index, also called a hash code,
 into an array of buckets or slots, from which
 the desired value can be found.

This script requires that `linkedList` and `wrapper` be imported within the Python
environment you are running this script in.

If imported into another file the module contains the following
functions:

    * keys - Return a list of all keys in this hash table.
    * get - Return the value associated with the given key, or raise KeyError.
    * set - Insert or update the given key with its associated value.
    * bucket_index - Return the bucket index where the given key would be stored.
    * values - Return a list of all values in this hash table.
    * items - Return a list of all items (key-value pairs) in this hash table.
    * length - Return the number of key-value entries by traversing its buckets.
    * contains - Return True if this hash table contains the given key, or False.
    * delete - Delete the given key from this hash table, or raise KeyError.
    * find - Search for a given item within the table

"""


# Built-in Python Modules
import time
import sys
import os

# local Python Modules
from linkedlist import LinkedList
from wrapper import time_it as benchmark


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for _ in range(
            init_size)]  # Create a new list (used as fixed-size array) of empty linked lists
        self.size = 0  # initialize size to 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __iter__(self):
        """Method returns the iterator object itself."""
        for bucket in self.buckets:
            for item in bucket.items():
                yield item
    
    def __len__(self):
        """Returns the length of the table"""
        return self.length()

    @benchmark
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    @benchmark
    def find(self, key):
        """Return item and bucket for a given key."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # find the item from the given key
        item = bucket.find(lambda item: item[0] == key)
        # return the item, bucket
        return item, bucket

    @benchmark
    def keys(self):
        """Return a list of all keys in this hash table."""
        """ 
            Time Complexity
            ---------------
                Best Case: O(1)Searching for first key
                Average Case: Θ(n) Every bucket only has 1 item
                Worst Case: Ω(n) We loop through every bucket, and then every item in each bucket
        """
        for bucket in self.buckets:
            for key, value in bucket.items():
                yield key

    @benchmark
    def values(self):
        """Return a list of all values in this hash table."""
        """ Time Complexity
            ---------------
                Best Case: O(1) if we only have one bucket that means we have one item
                Average Case: Θ(n) we only have to iterate over n buckets because each bucket contains 1 item
                Worst Case: Ω(n) we only have to iterate over n buckets because each bucket contains 1 item
        """
        # initialize an empty list of all the values
        values = []
        # loop through all de buckets
        for bucket in self.buckets:
            # append each value to a bucket
            for key, value in bucket.items():
                values.append(value)

        return values # return all values

    @benchmark
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table."""
        """ Time Complexity
            ---------------
                Best Case: O(1) Only searching for first bucket
                Average Case: Θ(n) Every bucket only has 1 item
                Worst Case: Ω(n) Every bucket has multiple items
        """
        items = []
        for bucket in self.buckets:
            items.extend(bucket.items())
        return items

    @benchmark
    def length(self):
        """Return the number of key-value entries by traversing its buckets."""
        """ Time Complexity
            ---------------
                Best Case: O(1) A return statment is constant
                Average Case: Θ(1) We calculate length in our set and delete functions
                Worst Case: Ω(1) A return statment is constant
        """
        return self.size

    @benchmark
    def contains(self, key):
        """Return True if this hash table contains the given key, or False."""
        """ Time Complexity
            ---------------
                Best Case: O(1)  every bucket has 1 item
                Average Case: Θ(1) every bucket has 1 item
                Worst Case: Ω(n) if there are too many items hashed in a single bucket
        """
        # get item and bucket
        item, bucket = self.find(key)

        # if item is found return true otherwiese false
        if item:
            return True
        return False

    @benchmark
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError."""
        """ Time Complexity
            ---------------
                Best Case: O(1) only need to check 1 operation
                Average Case: Θ(1) each bucket only has 1 item
                Worst Case: Ω(n) if there are too many items hashed in a single bucket.
        """
        item, bucket = self.find(key)
        # if item exists return the value associated with the key. otherwise raise KeyError if item was not found
        if item:
            return item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    @benchmark
    def set(self, key, value):
        """Insert or update the given key with its associated value."""
        """ Time Complexity
            ---------------
                Best Case: O(1) only need to check 1 operation
                Average Case: Θ(1) each bucket only has 1 item
                Worst Case: Ω(n) if there are too many items hashed in a single bucket.
        """
        # get the item and the bucket
        item, bucket = self.find(key)

        # if item exists, replace it with item. otherwise append it to that bucket
        if item:
            bucket.replace(item, (key, value))
        else:
            bucket.append((key, value))
            self.size += 1

    @benchmark
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError."""
        """ Time Complexity
            ---------------
                Best Case: O(1) the item we are deleting is the first
                Average Case: Θ(1) every bucket only has 1 item
                Worst Case: Ω(n) if there are too many items hashed in a single bucket.
        """
        item, bucket = self.find(key)
        # if item exists, delete it. otherwise raise KeyError that item was not found
        if item:
            bucket.delete(item)
            self.size -= 1
        else:
            raise KeyError('Key not found: {}'.format(key))

################# Alan's tests ####################


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


################# Alan's tests ####################

if __name__ == '__main__':
    test_hash_table()
