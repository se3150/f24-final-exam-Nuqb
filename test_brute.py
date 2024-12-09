import pytest
from brute import Brute

def describe_Brute():
    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        def it_succeeds_when_guess_is_correct(cracker):
            assert cracker.bruteOnce("TDD") == True

        def it_fails_when_guess_is_incorrect(cracker):
            assert cracker.bruteOnce("wrong") == False

    def describe_bruteMany():
        def it_succeeds_when_correct_guess_is_made(mocker):
            b = Brute("correct_guess")
            mocker.patch.object(b, 'randomGuess', return_value="correct_guess")
            assert b.bruteMany(100) > 0

        def it_fails_when_no_correct_guess_is_made(mocker):
            b = Brute("correct_guess")
            mocker.patch.object(b, 'randomGuess', return_value="wrong_guess")
            assert b.bruteMany(100) == -1

        def it_verifies_method_calls(mocker):
            b = Brute("correct_guess")
            random_mock = mocker.patch.object(b, 'randomGuess', return_value="wrong_guess")
            hash_mock = mocker.patch.object(b, 'hash', wraps=b.hash)

            b.bruteMany(10)

            random_mock.assert_called()
            hash_mock.assert_called()
