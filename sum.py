import os
import time
import shutil


def leapyear(y):
    if y % 400 == 0:
        return 29
    else:
        if y % 4 == 0:
            return 29
        else:
            return 28


name = ['SUN', 'MON', 'TUES', 'WED', 'THRUS', 'FRI', 'SAT']
today = 3
year = 2020
month = 5
day = 27
hrs = 12
mins = 26
sec = int(input())
while 1:
    if month <= 12:
        if month == 2:
            unknown = leapyear(year)
        else:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                unknown = 31
            else:
                unknown = 30
        if day <= unknown:
            if hrs < 24:
                if mins < 60:
                    if sec < 60:
                        # produce delay #
                        time.sleep(0.75)
                        # produce delay #
                        os.system('cls')
                        columns = shutil.get_terminal_size().columns
                        rows = shutil.get_terminal_size().lines
                        for i in range(int(rows / 2)):
                            print()
                        print("########################################".center(columns))
                        print("{}:{}:{}".format(day, month, year).center(columns))
                        print()
                        print("{}:{}:{}".format(hrs, mins, sec).center(columns))
                        print()
                        print("Today : {}".format(name[today]).center(columns))
                        print("########################################".center(columns))
                        sec += 1
                    else:
                        sec = 0
                        mins += 1
                else:
                    mins = 0
                    hrs += 1
            else:
                hrs = 0
                day += 1
                today += 1
                today = today % 7
        else:
            day = 1
            month += 1
    else:
        month = 1
        year += 1
