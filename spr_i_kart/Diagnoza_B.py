# Diagnoza INF

# - WSTĘP
# 1. Oblicz sumę liczb 3-cyfrowych
# suma=0
# for i in range(100,1000):
#   suma=suma+i
# print(suma)

# 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
# suma=0
# ilo=0
# for i in range(10,100):
#   if i%6==0:
#     suma=suma+i
#     ilo+=1
# print(f"{suma} i {ilo}")

# 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
# import random
# T=[]
# x=0
# for i in range(5):
#   x=random.randint(1000, 9999)
#   T.append(x)
# n=max(T)
# print(T)
# print(n)

# 4. Podaj sumę cyfr w dowolnej liczbie
# suma=0
# n=int(input("Podaj liczbe: "))
# while n>0:
#   suma=suma+n%10
#   n=n//10
# print(suma)

# 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
# T=[]
# n=int(input("Podaj liczbe: "))
# while n>0:
#   T.append(n%10)
#   n=n//10
# print(min(T))

# - ALGORYTMY
# 1. Sprawdź czy wpisana przez usera liczba jest pierwsza
# n=int(input("Podaj liczbe: "))
# f=True
# for i in range(2,n):
#   if n%i==0:
#     f=False
# if f==True:
#   print("Liczba jest pierwsza")
# else:
#   print("Liczba nie jest pierwsza")

# 2. Sprawdź czy wpisana przez usera liczba jest złożona
# n=int(input("Podaj liczbe: "))
# f=True
# for i in range(2,n):
#   if n%i==0:
#     f=False
# if f==True:
#   print("Liczba nie jest złożona")
# else:
#   print("Liczba jest złożona")

# 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24
# a=int(input("Podaj liczbe: "))
# b=24
# while(a!=b):
#   if a>b:
#     a=a-b
#   else:
#     b=b-a
# if a==1:
#   print("Podana liczba jest wzglednie pierwsza z 24.")
# else:
#   print("Podana liczba nie jest wzglednie pierwsza z 24.")

# 4. Zakoduj szyfrem CEZARA i kluczem k słowo s.
# s = input("Napisz napis: ")
# k=int(input("Podaj klucz: "))
# szyfr = ""
# for i in range(len(s)):
#   szyfr = szyfr + chr((ord(s[i])+ k))
# print(szyfr)

# 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.
# a=int(input("Podaj liczbe: "))
# b=int(input("Podaj liczbe: "))
# c=int(input("Podaj liczbe: "))
# d=int(input("Podaj liczbe: "))
# x = d*b
# while d!=b:
#   if d>b:
#     d=d-b
#   elif b>d:
#     b=b-d
# x=x//b
# a=a//b
# c=c//d
# l=a+c
# if l%x==0:
#   l=l//x
# if l>x:
#   e=l//x
#   l=l-e*x
#   print(e, l,"/",x)
# else:
#   print(l,"/",x)

# 6. Znajdź NWW dwóch wpisanych przez usera liczb
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = a*b
# while a!=b:
#   if a>b:
#     a=a-b
#   elif b>a:
#     b=b-a
# print(c//a)

# - NAPISY
# 1. Znajdź ilość liter C we wpisanym napisie
# n = input("Napisz napis: ")
# n=list(n)
# ilo=0
# for i in n:
#   if(n[i]=="C" or n[i]=="c"):
#     ilo+=1
# print(ilo)

# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp
# n=input("Napisz napis: ")
# T=[]
# x=0
# y=0
# for i in n:
#   T[i]=ord(n[i])
#   y=y+1
# for j in range(1,T):
#   if(T[j]>T[j-1]):
#     x=x+1
# if x==y:
#   print("TAK")
# else:
#   print("NIE")

# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.
# a=input("Napisz napis: ")
# b=input("Napisz napis: ")
# c=input("Napisz napis: ")
# x=0
# y=0
# z=0
# for i in a:
#   x+=1
# for i in b:
#   y+=1
# for i in c:
#   z+=1
# if x>y and x>z:
#   print(a)
# if z>y and x<z:
#   print(c)
# if x<y and y>z:
#   print(b)
