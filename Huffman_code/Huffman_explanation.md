
Problem 3 "Huffman Code" 



Objective
First, build the Huffman tree (a binary tree), and then generate the encoded data.  



Approach

To get the encoded data, We count the frecuency of each char, then build the tree where the leaf nodes are
the chars, the depth of each one in the tree is build by their frecuency in the values. 



Data Structure used: Binary tree


Efficiency :

    Time complexity:
        
        * encoding O(nlogn) -> Because it takes O(n) time to create the tree and takes O(nlogn) to create the huffman table.   
                
        
        * decoding O(nlog)n -> Because it takes O(n) time to read all the characters and takes O(nlogn) to read each of the                                      element of the tree. 
                 
               

    Space complexity:
    
       * encoding O(logn) -> Because the data is compressed.  
       
       * decoding O(nlogn) ->  Because the data is decompressed. 