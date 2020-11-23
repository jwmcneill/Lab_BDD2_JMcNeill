Feature: Social Security Full Retirement Age Calculator
  As a retiree, I want to know the age (with additional months) for obtaining full SSA benefits.

    Scenario Outline: Valid user input for retirement age
    Given The program full_retirement_age.py is executed, and prompts user to input year of birth
    When User inputs valid "<birth_year>"
    Then Program returns the correct "<age_years>" and "<age_months>"

    Examples:
      |birth_year|age_years|age_months|
      |1900      |65      |0          |
      |1937      |65      |0          |
      |1938      |65      |2          |
      |1939      |65      |4          |
      |1940      |65      |6          |
      |1941      |65      |8          |
      |1942      |65      |10         |
      |1943      |66      |0          |
      |1954      |66      |0          |
      |1955      |66      |2          |
      |1956      |66      |4          |
      |1957      |66      |6          |
      |1958      |66      |8          |
      |1959      |66      |10         |
      |1960      |67      |0          |
      |2000      |67      |0          |

  Scenario Outline: Valid user input for retirement date
    Given The program full_retirement_age.py is executed, and prompts user to input year of birth
    When User inputs valid "<birth_year>" and "<birth_month>" And Program returns correct "<age_years>" and "<age_months>"
    Then Program outputs the correct "<date_year>" and "<date_month>"

    Examples:
      |birth_year|birth_month|age_years|age_months|date_year|date_month|
      |1900      |1          |65       |0         |1965     |1         |
      |1937      |2          |65       |0         |2002     |2         |
      |1938      |3          |65       |2         |2003     |5         |
      |1940      |5          |65       |6         |2005     |11        |

  Scenario Outline: Invalid year user input
    Given The program full_retirement_age.py is executed, and prompts user to input year of birth
    When User inputs invalid year "<input>"
    Then Year returns "<valid>"

    Examples:
      |input|valid|
      |1899 |False|
      |3000 |False|
      |x    |False|
      |2020 |True |

  Scenario Outline: Invalid month user input
    Given The program full_retirement_age.py is executed, and prompts user to input year of birth
    When User inputs invalid month "<input>"
    Then Month returns "<valid>"

    Examples:
      |input|valid|
      |0    |False|
      |21   |False|
      |x    |False|
      |7    |True |
