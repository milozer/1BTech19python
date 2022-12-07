#Funkcja ord() - zwraca kod ASCII znaku
# print(ord("A"))
# print(ord("Z"))
# W Python kod ASCII wielkich liter A - Z sąod 65 do 90

#Funkcja cht() - zwraca znak dla danego kodu
# print(chr(66))
# print(chr(75))

# Zadanie testowe: Wypisz alfabet liter wielkich
# for i in range(65,91):
#   print(chr(i), end="")

# String w python - "lista"

napis = input("Podaj coś do zaszyfrowania: ")
szyfr = ""
print(napis[0], napis[1], napis[2])
print(len(napis))

for i in range(len(napis)):
  print(napis[i])
  szyfr = szyfr + chr(ord(napis[i])+3)
print(szyfr)