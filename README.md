TEST CASES

CALCULATOR TEST CASE

The standard workflow is:
1. You define your own class derived from unittest.TestCase.
2. Then you fill it with functions that start with ‘test_’.
3. You run the tests by placing unittest.main() in your file, usually at the bottom.
This is a pass test ,it checks whether the products of two inputs gives the right answer.the test fails if the expected output is not returned

```python
import unittest
from math import *
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')
 
if __name__ == '__main__':
unittest.main()
```





```python

import unittest

class ToRomanBadInput(unittest.TestCase):                            
    def testTooLarge(self):                                          
        #toRoman should fail with large input i.e inputs greater tha 9999                 
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 10000) 

    def testZero(self):                                              
        #toRoman should fail with 0 input                      
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)    

    def testNegative(self):                                          
        #toRoman should fail with negative input                
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)  

    def testNonInteger(self):                                        
        #toRoman should fail with non-integer input             
        self.assertRaises(roman.NotIntegerError, roman.toRoman, 0.5) 
if __name__ == '__main__':#4 failed test cases
unittest.main()
```

