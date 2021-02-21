Problem 4 "Active Directory" 



Objective

Write a function that provides an efficient look up of whether the user is in a group. 



Approach

We apply recursion, starting from the root, checking if the user is present in each group visited, if the user is found then it returns True, false otherwise. 


Data Structure used: Lists 


Efficiency :

    Time complexity:
        
        * O(n) -> Because n is the size of all the lists. 
      
    Space complexity:
    
        * O(n) -> Because we used 2 lists to stored groups and users. 
