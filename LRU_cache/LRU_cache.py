import collections


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        print("Cache starts with a capacity of:", capacity)
        self.max_cap = capacity
        self.dict = collections.OrderedDict()

    def get(self, key):
        """
        Get function: Get item from provided key
        Input: 
            self and key value
        Output:
            value -> item from provided key 
            -1 -> if item from procvided key nonexistent   
        """

        print('Get Element with Key')
        if key in self.dict:
            try:
                value = self.dict.pop(key)
                print(key)
                self.dict[key] = value
                return value
            except Exception as e:
                print(e)
                return -1
        else:
            return -1

    def set(self, key, value):
        """
        Set function: Set value if the key is not present in the cache, if the cache is at
                      capacity remove the oldest item. 
        Input: 
            self, key and value
        Output:
            Messages: null keys or  0 capacity cache    
        """
        if self.max_cap == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        if key is None:
            print("Can't set null keys")
            return

        try:
            self.dict.pop(key)
        except:
            if len(self.dict) >= self.max_cap:
                self.dict.popitem(last=False)

        self.dict[key] = value


# Test case 1

if __name__ == '__main__':
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1)      # returns 1
    our_cache.get(2)      # returns 2
    our_cache.get(9)      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    our_cache.get(3)
    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


print('\n-----------------------------------\n')


# Test Case 2
our_cache = LRU_Cache(0)
#expected: "Can't perform operations on 0 capacity cache"
our_cache.set(2, 4)
print(our_cache.get(20))  # expected: -1

print('\n-----------------------------------\n')


# Test case 3

our_cache = LRU_Cache(2)
our_cache.set(None, None)  # expected: Can't set null keys
print(our_cache.get(4))  # expected: -1
