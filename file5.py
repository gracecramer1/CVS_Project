# 1. use min and max columns
# 2. use station name to automatically generate an appropriate title
# 3. create two subplots in one vis
# 4.

import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)


# the enumerate() function returns both the index of
# each item and the value of each # item as you loop
# through a list.

for index, column_header in enumerate(header_row):
    print("Index: ", index, "Column Name: ", column_header)

highs = []
dates = []
lows = []


for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)


open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file2)


for index2, column_header2 in enumerate(header_row2):
    print("Index: ", index2, "Column Name: ", column_header2)

sitka_highs = []
sitka_dates = []
sitka_lows = []


for row2 in csv_file2:
    try:
        sitka_high = int(row2[5])
        sitka_low = int(row2[6])
        sitka_converted_date = datetime.strptime(row2[2], "%Y-%m-%d")

    except ValueError:
        print(f"missing data for {sitka_converted_date}")
    else:
        sitka_highs.append(sitka_high)
        sitka_lows.append(sitka_low)
        sitka_dates.append(sitka_converted_date)


import matplotlib.pyplot as plt

fig, a = plt.subplots(
    2,
)

a[0].plot(dates, highs, c="red")
a[0].plot(dates, lows, c="blue")

fig.autofmt_xdate()

a[0].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
a[0].set_title("DEATH VALLEY, CA US", fontsize=16)
a[0].set_xlabel("", fontsize=12)
a[0].set_ylabel("Temperature (F)", fontsize=12)
a[0].tick_params(axis="both", which="major", labelsize=12)


a[1].plot(sitka_dates, sitka_highs, c="red")
a[1].plot(sitka_dates, sitka_lows, c="blue")

fig.autofmt_xdate()

a[1].fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor="blue", alpha=0.1)
a[1].set_title("SITKA AIRPORT, AK US", fontsize=16)
a[1].set_xlabel("", fontsize=12)
a[1].set_ylabel("Temperature (F)", fontsize=12)
a[1].tick_params(axis="both", which="major", labelsize=12)

plt.show()

"""
a[0].title("", fontsize=16)
a[0].xlabel("", fontsize=12)
a[0].ylabel("Temperature (F)", fontsize=12)
a[0].tick_params(axis="both", which="major", labelsize=12)
"""
"""
ax[0].plot(dates, highs, c="red")
ax[0].plot(dates, lows, c="blue")

fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title(row[1], fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.show()

fig2, a = plt.subplots(2)
a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
"""
