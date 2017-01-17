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
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)