CALCULATOR TEST CASE

The standard workflow is:
1. You define your own class derived from unittest.TestCase.
2. Then you fill it with functions that start with ‘test_’.
3. You run the tests by placing unittest.main() in your file, usually at the bottom.

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

