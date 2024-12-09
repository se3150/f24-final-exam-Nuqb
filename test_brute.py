import pytest
from brute import Brute
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def cracker():
    return Brute("TDD")

def describe_Brute():

    def describe_bruteOnce():
        def it_returns_true_when_guess_is_correct(cracker):
            assert cracker.bruteOnce("TDD") == True

        def it_returns_false_when_guess_is_incorrect(cracker):
            assert cracker.bruteOnce("NotTDD") == False

        def it_returns_false_with_empty_string(cracker):
            assert cracker.bruteOnce("") == False

    def describe_bruteMany():
        def it_returns_time_when_cracked(cracker):
            mock = Mock()
            mock.return_value = "TDD"
            cracker.randomGuess = mock
            result = cracker.bruteMany(limit=10)
            assert result != -1
            mock.assert_called()

        def it_returns_negative_one_when_not_cracked(cracker):
            mock = Mock()
            mock.return_value = "NotCorrect"
            cracker.randomGuess = mock
            result = cracker.bruteMany(limit=5)
            assert result == -1
            assert mock.call_count == 5
