import unittest
from FizzBuzz import *

class TestFizzBuzz (unittest.TestCase) :

    def setUp(self) :
        self.instance=FizzBuzz()

    def test_affiche(self) :
        with self.subTest(self) :
            self.assertEqual(self.instance.affiche(100), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FrisBee3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FrisBee4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FrisBee6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FrisBee7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FrisBee9192Fizz94BuzzFizz9798FizzBuzz")
        with self.subTest(self) :
            self.assertEqual(self.instance.affiche(15), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")
    
    def tearDown(self) :
        pass


if __name__=='__main__' :
    unittest.main()