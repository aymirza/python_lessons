from datetime import datetime
import locale

now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%d/%m/%y"))
print(now.strftime("%d %B %Y (%A) "))
print(now.strftime("%d/%m/%y %I:%M"))
print("\n")


locale.setlocale(locale.LC_ALL, "")
now = datetime.now()
print(now.strftime("%d %B %Y (%A)"))

