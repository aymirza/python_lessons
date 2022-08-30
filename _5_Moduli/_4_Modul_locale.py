import locale

locale.setlocale(locale.LC_ALL, "de")

number = 12345.6789
formatted = locale.format_string("%f",number)
print(formatted)

formatted = locale.format_string("%.2f",number)
print(formatted)

formatted = locale.format_string("%d", number)
print(formatted)

formatted = locale.format_string("%e", number)
print(formatted)

money = 234.678
formatted = locale.currency(money)
print(formatted)

locale.setlocale(locale.LC_ALL, "")
number = 12345.6789
formatted = locale.format_string("%.02f",number)
print(formatted)
print(locale.getlocale())

