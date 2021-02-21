
Problem 6 "Union and Intersections" 


Objective

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. 



Approach

For the Union, We iterate over each element then we add each node to the new LinkedList. And for the intersection, We iterate over the second list 2 per item in list 1, and check if item exist in list 2, if its true append to the new linked list.


Data Structure used: LinkedLists


Efficiency :

    Time complexity:
        
        * union O(n + m) -> Because n is the size of the input in union.
        
        * intersection O(n * m) -> Because n are the elements of the list 1 and m are the elements of list                                    2, then We need to iterate for each elem in list 1 all the elements of                                      list 2. 
       
    Space complexity:
    
        * O(n + m) ->  Because n + m is the size of the LinkedLists. 

