# n = 12345
# print(n%100)
# print(n%10)
# print((n%1000)//100)

#from math import sqrt
# print(sqrt(576))
# print(576**(1/2))
# print(8**(1/3))


#ifyyyyyy

# == >= <= > < != -- operatory porównań

#pętla z liczbami 3-cyfrowymi podzielnych przez 13 i niepodzielnych przez 4

# for i in range(100,1000):
#   if i % 13 == 0 and i % 4 != 1:
#     print(i, end=" ")


#łączenie warunków

# a, b, c = 3, 5, 7
# if a < b < c:
#   if a < b and b < c:
#     print("Eppure si move")


# n = 24
# suma = 0
# ilosc = 0
# for i in range(1,25):
#   if n % i == 0:
#     print(i)
#     suma = suma + i
#     ilosc = ilosc + 1

# print("suma", suma)
# print("ilosc", ilosc)



#oblicz sume k początkowych liczb trzycyfrowych
# 100 + 101 +102 + 103 ...
# we: 4
# wy: 406 (100+101+102+103)

# k = 4
# suma = 0
# ilosc = 0
# for i in range(100, 1000):
#   suma = suma+i
#   ilosc = ilosc + 1
#   if ilosc == k:
#     break
# print(suma)



# k = 4
# suma = 0
# for i in range(100, 100+k):
#   suma = suma+i
# print(suma)


#oblicz sume n początkowych wyrazów ciągu fibonacciego
#1+2+3+5+8+13...

# n = int(input())
# a, b = 0, 1
# suma= 0
# for i in range(n):
#   a, b = b, a+b
#   suma = suma +b
# print(suma)
