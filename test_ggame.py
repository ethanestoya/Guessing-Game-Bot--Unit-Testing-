# Adding Unit Tests to Remote Guessing Game
    
    # How would you apply 100% test coverage for your application?
    # How to use mocks in testing applications?
    # How do you make your application testable?
    
import unittest
from unittest.mock import MagicMock

from ggame import generate_random, get_difficulty

class TestGGame(unittest.TestCase):
    
    def test_generate_random(self):
        self.assertTrue(1 <= generate_random(1) <= 10)
        self.assertTrue(1 <= generate_random(2) <= 50)
        self.assertTrue(1 <= generate_random(3) <= 100)

    def test_get_difficulty(self):
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'2'

        difficulty = get_difficulty(mock_socket)
        self.assertEqual(difficulty, 2)

if __name__ == '__main__':
    unittest.main()

# ESTOYA, ETHAN LAUREEN E.
# BSIT 2ND YEAR - BLOCK 2