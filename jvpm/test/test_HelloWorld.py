import unittest
import sys
import jvpm.HelloWorld
from unittest.mock import Mock, call

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        sys.stdout = unittest.mock.Mock()
        jvpm.HelloWorld.HelloWorld()
        sys.stdout.assert_has_calls(
            [call.write('Hello world'), call.write('\n')]
        )
        sys.stdout.assert_has_calls(
            [call.write('Hello Kenji Morizono'), call.write('\n')]
        )
        sys.stdout.assert_has_calls(
            [call.write('Hello Ryan McCullough'), call.write('\n')]
        )
        sys.stdout.assert_has_calls(
            [call.write('Hello Ian Mutahi'), call.write('\n')]
        )
        sys.stdout.assert_has_calls(
            [call.write('Hello Carlos Olivas'), call.write('\n')]
        )
