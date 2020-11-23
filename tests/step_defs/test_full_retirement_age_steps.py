from pytest_bdd import scenarios, parsers, given, when, then

import full_retirement_age

CONVERTERS = {
    'input': int,
    'valid': int,
    'birth_year': int,
    'birth_month': int,
    'age_years': int,
    'age_month': int,
    'date_year': int,
    'date_month': int,
}

scenarios('../features/full_retirement_age.feature', example_converters=CONVERTERS)


@given('the program full_retirement_age.py is executed, and prompts user to input year of birth')
def initial():
    pass


@when('User inputs valid "<birth_year>"')
def input_invalid_month(birth_year):
    full_retirement_age.calculate_retirement_age(birth_year)


@then('Program returns the correct "<age_years>" and "<age_months>"')
def year_validation(birth_year, age_years, age_months):
    year, month = full_retirement_age.calculate_retirement_age(birth_year)
    assert year == int(age_years)
    assert month == int(age_months)


@when('User inputs valid "<birth_year>" and "<birth_month>" And Program returns correct "<age_years>" and '
      '"<age_months>"')
def input_invalid_month(birth_year, birth_month, age_years, age_months):
    full_retirement_age.calculate_retirement_date(birth_year, birth_month, age_years, age_months)


@then('Program outputs the correct "<date_year>" and "<date_month>"')
def year_validation(birth_year, birth_month, age_years, age_months, date_year, date_month):
    year, month = full_retirement_age.calculate_retirement_date(birth_year, birth_month, age_years, age_months)
    assert year == int(date_year)
    assert month == int(date_month)


@when('User inputs invalid year "<input>"')
def input_invalid_year(input):
    full_retirement_age._validate_birth_year(input)


@then('Year returns "<valid>"')
def year_validation(valid, input):
    assert str(full_retirement_age._validate_age_year(input)) == valid


@when('User inputs invalid month "<input>"')
def input_invalid_month(input):
    full_retirement_age._validate_birth_month(input)


@then('Month returns "<valid>"')
def year_validation(valid, input):
    assert str(full_retirement_age._validate_birth_month(input)) == valid
