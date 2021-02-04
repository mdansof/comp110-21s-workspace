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
population = input("Population: ")
population = int(population)
dosesAdmin = input("Doses administered: ")
dosesAdmin = int(dosesAdmin)
dosesDaily = input("Doses per day: ")
dosesDaily = int(dosesDaily)
perTarget = input("Target percent vaccinated: ")
perTarget = int(perTarget)
pplVaccinated = dosesAdmin // 2
popLeft = population - pplVaccinated
popLeft = int(popLeft)
perVac = (pplVaccinated / population) * 100
if perVac < float(perTarget) :
    perLeft = float(perTarget) - perVac
    pplNeedVaccine = (perLeft * population)/ 100
    daysNeed = round((pplNeedVaccine * 2) / dosesDaily)
    today: datetime = datetime.today()
    enddate: timedelta = timedelta(daysNeed)
    future: datetime = today + enddate
    print("We will reach " + str(perTarget
     ) + "% vaccination in "+ str(daysNeed) + " days, which falls on " + future.strftime("%B %d, %Y"))
else:
    print("we are there")


