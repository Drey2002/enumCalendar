from enum import Enum
import calendar

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

class Day(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def print_calendar(year):
    cal = calendar.Calendar()
    
    for month in Month:
        print(f"\n{month.name} {year}")
        print("Mo Tu We Th Fr Sa Su")

        for week in cal.monthdayscalendar(year, month.value):
            for day in week:
                if day == 0:
                    print("   ", end="")  # Print empty space for days not in the month
                else:
                    print(f"{day:2d} ", end="")
            print()  # Move to the next line for the next week

        print()

# Print the calendar for the year 2024
print_calendar(2024)
