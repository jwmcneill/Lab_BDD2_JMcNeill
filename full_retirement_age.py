# CSC256: Full Retirement Age - Jerry McNeill
import datetime


def _validate_age_month(month):
    month = int(month)

    if month < 0 or month > 11:
        raise ValueError(f'Age month "{month}" must be between 0 and 11')

    return month


def _validate_age_year(year):
    year = int(year)

    if year < 65 or year > 67:
        raise ValueError(f'Age year "{year}" must be between 65 and 67')

    return year


def _validate_birth_month(month):
    month = int(month)

    if month < 1 or month > 12:
        raise ValueError(f'Birth month "{month}" must be between 1 and 12')

    return month


def _validate_birth_year(year):
    year = int(year)

    if year < 1900:
        raise ValueError(f'Birth year "{year}" must be no earlier than 1900')
    elif year >= 3000:
        raise ValueError(f'Birth year "{year}" must be earlier than 3000')

    return year


def calculate_retirement_age(birth_year):
    birth_year = _validate_birth_year(birth_year)

    if birth_year <= 1937:
        return 65, 0
    elif birth_year == 1938:
        return 65, 2
    elif birth_year == 1939:
        return 65, 4
    elif birth_year == 1940:
        return 65, 6
    elif birth_year == 1941:
        return 65, 8
    elif birth_year == 1942:
        return 65, 10
    elif 1943 <= birth_year <= 1954:
        return 66, 0
    elif birth_year == 1955:
        return 66, 2
    elif birth_year == 1956:
        return 66, 4
    elif birth_year == 1957:
        return 66, 6
    elif birth_year == 1958:
        return 66, 8
    elif birth_year == 1959:
        return 66, 10
    else:
        return 67, 0


def calculate_retirement_date(birth_year, birth_month, age_years, age_months):
    birth_year = _validate_birth_year(birth_year)
    birth_month = _validate_birth_month(birth_month)
    age_years = _validate_age_year(age_years)
    age_months = _validate_age_month(age_months)

    year = birth_year + age_years
    month = birth_month + age_months

    if month > 12:
        year += 1
        month -= 12

    return year, month


def main():
    print("-Social Security Full Retirement Age Calculator-\n")

    birth_year = input("Input year of birth, or press enter to exit: ")
    while not _validate_birth_year(birth_year):
        input("Input year of birth, or press enter to exit: ")
        birth_month = input("Input month of birth (1-12): ")
        while not _validate_birth_month():
            input("Input month of birth (1-12): ")

    retire_age_year, retire_age_month = calculate_retirement_age(birth_year)
    retire_date_year, retire_date_month = calculate_retirement_date(birth_year, birth_month, retire_age_year,
                                                                    retire_age_month)
    month_name = datetime.date(2000, retire_date_month, 1).strftime("%B")

    print(f"\nYour full retirement age is {retire_age_year} and {retire_age_month} months.")
    print(f"This will be in {month_name} of {retire_date_year}")