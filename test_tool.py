import unittest
from tool import check
class Tests(unittest.TestCase):
 def test_limits(self): self.assertEqual(check(10,20,0,15,5),['out_of_range','step_too_large'])
if __name__=='__main__': unittest.main()
