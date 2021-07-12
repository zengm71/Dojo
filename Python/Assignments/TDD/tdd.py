# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def reverseList(l):
    for i in range(round((len(l)-1)/2)):
        print(i)
        l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
        print(l)
    return l
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
        self.assertEqual(reverseList([1,2,3,5]), [5,3,2,1])
        self.assertEqual(reverseList([1,2,3,4,5]), [5,4,3,2,1])

    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests


