
zakupy = [0.2, 0.5, 4.59, 6] #netto

#FAKTURY
def vat_faktura(lista):
    return 0.23*sum(lista)

def vat_paragon(lista):
    vat_all=0
    for i in lista:
        vat_all += i*0.23
    return(vat_all)



print("VAT faktura =",vat_faktura(zakupy))

print("VAT paragon =",vat_paragon(zakupy))

print(vat_faktura(zakupy) == vat_paragon(zakupy))


