"""
Find the year from your age ,when you will be become 100 years old
"""


import datetime as dt
age = int(input("Enter Your Age "))

cur_year = dt.datetime.now().year

next_year = (cur_year-age)+100

print("You will be 100 years old in year {} ".format(next_year))

