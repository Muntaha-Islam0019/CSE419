def find_age(current_date, current_month, current_year,
             birth_date, birth_month, birth_year):

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + days_in_months[birth_month-1]

    if (birth_month > current_month):
        current_year = current_year - 1
        current_month = current_month + 12

    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year

    print("Present Age: ")
    print("Years:", calculated_year, "; Months:",
          calculated_month, "; Days:", calculated_date)


def leap_or_not(year):

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("It's a leapyear.")
            else:
                print("It's not a leapyear.")
        else:
            print("It's a leapyear.")
    else:
        print("It's not a leapyear.")


print("Please enter current date info: ")
current_year = int(input("Year: "))
current_month = int(input("Month: "))
current_date = int(input("Date: "))

print("Please enter birth date info: ")
birth_year = int(input("Year: "))
birth_month = int(input("Month: "))
birth_date = int(input("Date: "))

find_age(current_date, current_month, current_year,
         birth_date, birth_month, birth_year)

leap_or_not(current_year)
