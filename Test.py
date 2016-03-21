import unittest
from Network import *

class TestNetwork(unittest.TestCase):

    def test_get_probability_with_value(self):
        value = bn.get_probability('LVEDVOLUME', evidence={'HYPOVOLEMIA': 'TRUE', 'LVFAILURE': 'TRUE'}, value='HIGH')
        self.assertEqual(float(value), 0.01)

    def test_sample_with_seed_r(self):
        sample = bn.sample('LVEDVOLUME', given={'HYPOVOLEMIA': 'TRUE', 'LVFAILURE': 'TRUE'}, r=0.011)
        self.assertEqual(sample, 'LOW')

    if "__name__" == "__main__":
        unittest.main()
