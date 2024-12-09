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
            assert cracker.bruteOnce("TDD") is True

        def it_returns_false_when_guess_is_incorrect(cracker):
            assert cracker.bruteOnce("NotTDD") is False

        def it_returns_false_with_empty_string(cracker):
            assert cracker.bruteOnce("") is False

        def it_returns_false_for_partial_match(cracker):
            assert cracker.bruteOnce("TD") is False

    def describe_bruteMany():
        def it_returns_time_when_cracked_immediately(cracker):
            mock = Mock(return_value="TDD")
            cracker.randomGuess = mock

            result = cracker.bruteMany(limit=10)
            assert result != -1
            mock.assert_called_once()

        def it_returns_negative_one_if_not_found(cracker):
            mock = Mock(return_value="NotTDD")
            cracker.randomGuess = mock

            result = cracker.bruteMany(limit=5)
            assert result == -1
            assert mock.call_count == 5

        def it_handles_zero_limit(cracker):
            result = cracker.bruteMany(limit=0)
            assert result == -1

        def it_can_crack_with_small_limit(cracker):
            mock = Mock(side_effect=["Wrong", "TDD"])
            cracker.randomGuess = mock

            result = cracker.bruteMany(limit=2)
            assert result != -1
            assert mock.call_count == 2

        def it_cracks_on_last_attempt(cracker):
            mock = Mock(side_effect=["Wrong1", "Wrong2", "TDD"])
            cracker.randomGuess = mock

            result = cracker.bruteMany(limit=3)
            assert result != -1
            assert mock.call_count == 3

        def it_returns_negative_one_with_multiple_random_guesses(cracker):
            mock = Mock(side_effect=["Guess1", "Guess2", "Guess3", "Guess4"])
            cracker.randomGuess = mock

            result = cracker.bruteMany(limit=4)
            assert result == -1
            assert mock.call_count == 4
