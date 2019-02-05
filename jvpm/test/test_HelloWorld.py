import unittest
import jvpm.HelloWorld
from unittest.mock import patch, call

class TestHelloWorld(unittest.TestCase):
    @patch('builtins.print')
    def test_HelloWorld(self, mock_print):
        jvpm.HelloWorld.HelloWorld()
        self.assertEqual(mock_print.mock_calls, [
            call('Hello world'),
            call('Hello Kenji Morizono'),
            call('Hello Ryan McCullough'),
            call('Hello Ian Mutahi'),
            call('Hello Carlos Olivas'),
            call('Hello Gerom Pagaduan'),
            call('Hello Tanner Madsen')
        ])
