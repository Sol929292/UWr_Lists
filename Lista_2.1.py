"""Zadanie 1. Zaprogramuj klasę Wyrazenie wraz z odpowiednimi podklasami
reprezentującymi rózne rodzaje wyrażeń arytmetycznych.
Przykładowo, wyrażenie      (x + 2) * y
może być reprezentowane jako:

Razy(Dodaj(Zmienna("x"), Stala(2)), Zmienna("y"))

gdzie Razy, Zmienna czy Stala są odpowiednimi podklasami klasy Wyrazenie.
Zaprogramuj w każdej klasie metodę oblicz(self, zmienne), która oblicza
wartość wyrażenia; przy czym argument zmienne przechowuje informacje o tym,
jakie wartości mają odpowiednie zmienne.

1) Zaprogramuj własne wyjątki reagujące na niepoprawne sytuacje, np. dzielenie
przez zero czy brak przypisania wartości zmiennej.
Wymagane jest, aby były zdefiniowane stałe, zmienne i podstawowe działania
arytmetyczne.

2) Następnie w podobny sposób zaprogramuj hierarchię klas reprezentującą prosty
język programowania z instrukcją przypisania do zmiennej, instrukcją warunkową
i pętlą. Możesz przyjąć, że wyrażenie równe zero interpretujemy jako fałsz, a
prawdę w przeciwnym przypadku. W każdej z tych klas zaprogramuj metodę
wykonaj(self, zmienne) wykonującą instrukcje.

3)We wszystkich powyższych klasach zaprogramuj metodę __str__ zwracającą
jako string ładnie sformatowane wyrażenie bądź program."""

class Wyrazenie:
    pass

class Zmienna(Wyrazenie):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Stala(Wyrazenie):
    def __init__(self, stala):
        self.stala = stala

class Dodaj(Wyrazenie):
    def oblicz(self, x, y):
        return x + y

class Razy(Wyrazenie):
    def oblicz(self, x, y):
        return x * y

# Samples:
zmienna_x = Zmienna("x", 10)
print(zmienna_x.name, zmienna_x.value)  # x 10

zmienna_y = Zmienna("y", 3)
print(zmienna_y.name, zmienna_y.value)  # y 3

stala_2 = Stala(2)
print(stala_2.stala)    # 2
print(stala_2)    # <__main__.Stala object at 0x0000022022C1BD30>


