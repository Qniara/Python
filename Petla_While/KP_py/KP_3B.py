# Zad.1
# i=0
# while(i<=30):
#   i+=1
#   print(i)

# Zad.2
# i=-1
# while i<=9:
#   i+=2
#   print(i**2)

# Zad.3
# i=1000
# while i<=9999:
#   if(i%379==0):
#     print(i)
#   i=i+1

# Zad.4
# i=100
# while i<=999:
#   if (i%5==0 and i%6==0) or i%11==0:
#     print(i, end=" ")
#   i=i+1

# Zad.5
# n=int(input("Podaj ile liczb podasz: "))
# i=1
# suma=0
# while i<=n:
#   x=int(input("Podaj liczbe: "))
#   suma=suma+x
#   i=i+1
# print("Suma liczb jest rowna: ", suma)

# Zad.6
# k= int(input("Podaj liczbe: "))
# i = 0
# suma=0
# while i < k:
#   i=i+2
#   suma=suma+i
# print("Suma", k, "liczb jest rowna: ", suma)

# Zad.7
# m =int(input("Podaj liczbe: "))
# i = 11
# suma=0
# while i < m:
#   i = i + 2
#   suma=suma+i
# print("Suma", m, "liczb jest rowna: ", suma)

# Zad.8
# wej=int(input("Podaj liczbe: "))
# l=float(input("Podaj liczbe: "))
# k=0.06
# wyj=0
# i=0
# while i<=l:
#   i+=1
#   wyj=wyj+wej*k
# print("Kwota koncowa to: ", wyj)

# Zad.9
# n=int(input("Podaj liczbe: "))
# i=0
# while i<n*100:
#   if i%100==21:
#     print(i)
#   i=i+1

# Zad.10
# import math
# i=1
# while(i<=1000):
#   if(i<100):
#     if(i%10==math.sqrt(i)):
#       print(i)
#   elif(i<1000):
#     if(i%100==math.sqrt(i)):
#       print(i)
#   i=i+1