Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.


Background:
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"

Scenario: I can successfully encode a secret message
    When I set "hello world" to the inputfield "#letters"
    When I click on the element "#shift-amount"
    When I select the option with the value "1" for element "#shift-amount"
    When I click on the element "#submit"
    When I pause for 1000ms
    Then I expect that element "#decoded_message" contains the text "ifmmp xpsme"

Scenario: I can successfully decode a secret message
    When I set "ifmmp xpsme" to the inputfield "#letters"
    When I click on the element "#shift-amount"
    When I select the option with the value "1" for element "#shift-amount"
    When I click on the element "#decoder-setting"
    When I select the option with the value "D" for element "#decoder-setting"
    When I click on the element "#submit"
    When I pause for 1000ms
    Then I expect that element "#decoded_message" contains the text "hello world"
