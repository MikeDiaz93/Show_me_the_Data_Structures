
Problem 1 "LRU cache" 



Objective

The goal will be to design a data structure known as a Least Recently Used (LRU) cache, which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation. 


Approach

We apply ordered dicts, where each value is add with its respective key to the cache memory, and put it in the hashmap (key reference). 



Data Structure used: Hashmaps 


Efficiency :

    Time complexity:

    * get O(1) -> because our dictionary can have a constant complexity. 
    * set O(n) -> because we just need to iterate each value of the dictionary to find if the new element                     exist or not. 


    Space complexity:
    
    * O(1) -> Because we implement hashmaps and we can access directly to the one we're looking for. 

    