number = 0.1+0.1+0.1
print(number)

from decimal import Decimal
number = Decimal("0._1_Otkiritie_i_zakritie_faylovv")
number = number+number+number
print(number)

number = Decimal("0.10")
number = 3*number
print(number)
print("\n")

# Округление чисел quantize()

from decimal import Decimal

number = Decimal("0.444")
number = number.quantize(Decimal("_1_Otkiritie_i_zakritie_faylovv.00"))
print(number)

number = Decimal("0.555678")
print(number.quantize(Decimal("_1_Otkiritie_i_zakritie_faylovv.00")))

number = Decimal("0.999")
print(number.quantize(Decimal("_1_Otkiritie_i_zakritie_faylovv.00")))

