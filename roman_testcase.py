
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
