##Import the `datetime` module with an alias and use it to print the current date and time.
from datetime import*
now = datetime.now()
print(now)

##Use the `datetime` module to print the current date, calculate the date 100 days from today, 
#and determine the day of the week for a given date.

print("Current date : ",date.today())
print("100 days from today: ",date.today()+timedelta(100))
given_date = date(2026,2,12)
print("Day of the week for 2026-02-12: ",given_date.strftime('%A'))
