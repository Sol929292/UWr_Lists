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

from abc import ABC, abstractmethod

class Zmienna():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Zmienna({self.name})"


class Stala():
    def __init__(self, stala):
        self.stala = stala

    def __str__(self):
        return f"Stala({self.stala})"

#____________________________________________________________

class Dzialanie(ABC):
    @abstractmethod
    def oblicz(self):
        pass


class Dodaj(Dzialanie):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def oblicz(self): #Jesli nie zaimplementuje def oblicz - nie stworze obiektu dodaj (abstractmethod)
        return self.x + self.y

    def __str__(self):
        return f"Dodaj({self.x}, {self.y})"

class Razy(Dzialanie):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def oblicz(self):
        return self.x * self.y

    def __str__(self):
        return f"Razy({self.x}, {self.y})"

class Podziel(Dzialanie):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def oblicz(self):
        return self.x / self.y

    def __str__(self):
        return f"Razy({self.x}, {self.y})"


# Samples:
zmienna_x = Zmienna("x", 10)
print(zmienna_x.name, zmienna_x.value)  # x 10
print(zmienna_x)                        # Zmienna(x)

zmienna_y = Zmienna("y", 3)
print(zmienna_y.name, zmienna_y.value)  # y 3

stala_2 = Stala(2)
print(stala_2.stala)                    # 2
print(stala_2)                          # Stala(2)

dodaj = Dodaj(zmienna_x.value, stala_2.stala)

print(dodaj)                            # Dodaj(10, 2)
print(dodaj.oblicz())                   # 12

razy = Razy(dodaj.oblicz(), zmienna_y.value)
print(razy)                            # Razy(12, 3)
print(razy.oblicz())                   # 36

podziel = Podziel(6, 2)                 # 6/2 = 3
print(podziel.oblicz())

print("main__________________________________")
print(f"({zmienna_x.name} + {stala_2.stala}) * {zmienna_y.name} =")
print(f"({zmienna_x.value} + {stala_2.stala}) * {zmienna_y.value} =")

print(f"{dodaj.oblicz()} * {zmienna_y.value} = {razy.oblicz()}")

print(dodaj, razy, zmienna_x, zmienna_y)