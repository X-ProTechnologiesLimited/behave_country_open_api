# file:features/calculation.feature
Feature:Calculation

    Scenario Outline: Basic Calculation of 2 numbers
    Given I have 2 numbers "<x>" and "<y>"
    When I "<operate>" them
    Then I get the result "<result>"

    Examples: "<operate>", "<x>" and "<y>"
        | x  | y  |  operate  | relation | result |
        | 2  | 5  |  add      | with     | 7      |
        | 3  | 7  |  subtract | from     | 4      |
        | 9  | 2  |  multiply | with     | 18     |
        | 16 | 2  |  divide   | with     | 8      |