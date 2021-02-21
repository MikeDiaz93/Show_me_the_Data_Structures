Problem 2 "File Recursion" 


Objective

The goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c".


Approach

We implement recursion and iteration over each folder. So we traverse the given path to verify the suffix in the file We're looking for and add it to the list. 


Data Structure used: Lists 


Efficiency :

    Time complexity:
        
        * O(n) -> Because n is the number of files and folders in the given path.      

    Space complexity:
    
        * O(n) -> As n is the number of files and folders in the given path, then We                     could have a list with the n elements.    

    


