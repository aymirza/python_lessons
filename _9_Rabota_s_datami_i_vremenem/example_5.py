from datetime import timedelta, datetime


three_hours = timedelta(hours=3)
print(three_hours)

three_hours_thirty_minutes = timedelta(hours=3,minutes=30)
print(three_hours_thirty_minutes)

two_days = timedelta(2)
print(two_days)

two_days_three_hours_thirty_minutes = timedelta(days=2,hours=3,minutes=30)
print(two_days_three_hours_thirty_minutes)

now = datetime.now()
print(now)
two_days = timedelta(2)
in_two_days = now + two_days
print(in_two_days)
two_days_two_hours = timedelta(days=2,hours=2)
in_two_days_two_hours = now + two_days_two_hours
print(in_two_days_two_hours)
in_two_days_two_hours = now - two_days_two_hours
print(in_two_days_two_hours)
print("\n")

my_string = str(input("Enter date(yyyy-mm-dd): "))
deadline = datetime.strptime(my_string, "%Y-%m-%d")
print(deadline)
now = datetime.now()
print(deadline)
if now > deadline:
    print("Срок сдачи проекта прошел")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("Срок сдачи проекта сегодня")
else:
    period = deadline - now
    print("Осталось {} дней".format(period.days))




