"""A vaccination calculator."""

__author__ = "730316345"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population:int  = int(input("Population: "))
dosesAdmin:int  = int(input("Doses administered: "))
dosesDaily:int = int(input("Doses per day: "))
perTarget:int = int(input("Target percent vaccinated: "))

totalDosesToGive = (population * (perTarget/100)) * 2
dosesLeft = totalDosesToGive - dosesAdmin
daysLeft= round(dosesLeft/dosesDaily)

    
today: datetime = datetime.today()
enddate: timedelta = timedelta(daysLeft)
future: datetime = today + enddate
print("We will reach " + str(perTarget
     ) + "% vaccination in "+ str(daysLeft) + " days, which falls on " + future.strftime("%B %d, %Y"))



