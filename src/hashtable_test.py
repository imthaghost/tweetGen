from hashtable import HashTable
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):
#################### Alan tests ########################
    def test_init(self):
        ht = HashTable(4)
        assert len(ht.buckets) == 4
        assert ht.length() == 0

    def test_keys(self):
        ht = HashTable()
        assert list(ht.keys()) == []
        ht.set('I', 1)
        assert list(ht.keys()) == ['I']
        ht.set('V', 5)
        self.assertCountEqual(list(ht.keys()), ['I', 'V'])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(list(ht.keys()), ['I', 'V', 'X'])  # Ignore item order

    def test_values(self):
        ht = HashTable()
        assert list(ht.values()) == []
        ht.set('I', 1)
        assert list(ht.values()) == [1]
        ht.set('V', 5)
        self.assertCountEqual(list(ht.values()), [1, 5])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(list(ht.values()), [1, 5, 10])  # Ignore item order

    def test_items(self):
        ht = HashTable()
        assert ht.items() == []
        ht.set('I', 1)
        assert ht.items() == [('I', 1)]
        ht.set('V', 5)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5)])
        ht.set('X', 10)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5), ('X', 10)])

    def test_length(self):
        ht = HashTable()
        assert ht.length() == 0
        ht.set('I', 1)
        assert ht.length() == 1
        ht.set('V', 5)
        assert ht.length() == 2
        ht.set('X', 10)
        assert ht.length() == 3
    

    def test_contains(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.contains('I') is True
        assert ht.contains('V') is True
        assert ht.contains('X') is True
        assert ht.contains('A') is False

    def test_set_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3
        with self.assertRaises(KeyError):
            ht.get('A')  # Key does not exist

    def test_set_twice_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 4)
        ht.set('X', 9)
        assert ht.length() == 3
        ht.set('V', 5)  # Update value
        ht.set('X', 10)  # Update value
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3  # Check length is not overcounting
    
    def test_delete_non_existant_items(self):
        ht = HashTable()
        with self.assertRaises(KeyError):
            ht.delete('A')

    def test_delete(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.length() == 3
        ht.delete('I')
        ht.delete('X')
        assert ht.length() == 1
        with self.assertRaises(KeyError):
            ht.delete('X')  # Key no longer exists
        with self.assertRaises(KeyError):
            ht.delete('A')  # Key does not exist
################### Alan tests ###################
################### My Tests #####################
def test_set_after_delete(self):
        ht = HashTable()
        ht.set('G', 900)
        assert ht.get('G') == 900
        ht.delete('G')
        with self.assertRaises(KeyError):
            ht.get('G')
        ht.set('G', 900)
        assert ht.get('G') == 900

def test_set_multiple_and_get(self):
        ht = HashTable()
        ht.set('A', 0)
        ht.set('B', 1)
        ht.set('C', 2)
        ht.set('D', 3)
        ht.set('E', 4)
        ht.set('F', 5)
        ht.set('G', 6)
        ht.set('H', 7)
        ht.set('I', 8)
        assert ht.length() == 9
        ht.set('A', 5)  # Update value
        ht.set('B', 10)  # Update value
        assert ht.get('A') == 5
        assert ht.get('B') == 10
        assert ht.get('F') == 5
        assert ht.length() == 9  # Check length is not overcounting

def test_boolean_contains(self):
        ht = HashTable()
        ht.set('A', 1)
        ht.set('B', 5)
        ht.set('C', 10)
        assert ht.contains('A') is True
        assert ht.contains('B') is True
        assert ht.contains('C') is True
        assert ht.contains('G') is False
################### My Tests #####################


if __name__ == '__main__':
    unittest.main()
