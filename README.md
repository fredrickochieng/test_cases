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




 ROMAN TEST CASE
 
 
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

skipping testcase
Unittest supports skipping individual test methods and even whole classes of tests.It also supports marking a test as an “expected failure,” a test that is broken and will fail, but shouldn’t be counted as a failure on a TestResult.

Skipping a test is simply a matter of using the skip() decorator 


``python`
mport unittest

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
if __name__ == '__main__':#2 failed test cases
unittest.main()```


String method testcase


```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('idiot'.upper(), 'IDIOT')

    def test_isupper(self):
        self.assertTrue('IDIOT'.isupper())
        self.assertFalse('Idiot'.isupper())

    def test_split(self):
        s = 'hello Andela'
        self.assertEqual(s.split(), ['hello', 'Andela'])
        
        with self.assertRaises(TypeError):
            s.split(2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
```
