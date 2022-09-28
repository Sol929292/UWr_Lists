
"""Zadanie 2.
W portfelu znajdują się monety 1, 2 i 5 złotowe, a także banknoty 10 i 20 złotowe.
Za zakupy jest do zapłacenia 123 zł.
Można rachunek zapłacić na różne sposoby,
np. dając 123 złotówki albo sześć dwudziestozłotówek + jedna dwuzłotówka + złotówka.
Napisz program, który dla zadanej kwoty podaje jakie i ile
monet i banknotów mam wyjąć z portfela, aby łącznie wyjąć jak najmniej monet
i banknotów. Zakładam, że monet i banknotów mam zawsze wystarczająco dużo."""

amount = 123
nominal_value = [20, 10, 5, 2, 1]
quantity_value = []
unpaid = amount

for value in nominal_value:
    while unpaid >= 0:
        n = int(unpaid/value)
        print(n)
        unpaid -= n * value
        print(unpaid)
        if n > 0:
            quantity_value.append(n)
            break
        elif unpaid ==0: break
        else:
            quantity_value.append(n)
            break
    else:
        break


print(quantity_value)


def print_result(n, x, amount): # n - quantity, x - value
    print("You can pay by:")
    for i in range(0, len(n)):
        print(f"{n[i]} x {x[i]}$")

    print(f"Total amount to pay: {amount}$.")


print_result(quantity_value, nominal_value, amount)


