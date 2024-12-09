import pytest
from brute import Brute

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        def test_bruteOnce_success(cracker):
            assert cracker.bruteOnce("TDD") is True

        def test_bruteOnce_failure(cracker):
            assert cracker.bruteOnce("Wrong") is False

    def describe_bruteMany():
        def test_bruteMany_success(mocker, cracker):
            mocker.patch.object(cracker, "randomGuess", return_value="TDD")
            result = cracker.bruteMany(limit=10)
            assert result != -1

        def test_bruteMany_failure(mocker, cracker):
            mocker.patch.object(cracker, "randomGuess", return_value="NotCorrect")
            result = cracker.bruteMany(limit=5)
            assert result == -1
