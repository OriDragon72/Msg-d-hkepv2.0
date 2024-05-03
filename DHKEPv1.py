from sympy import randprime
import random

#A function made to generate a large prime number
def GLP():
  return randprime(10**1, 10**3)

#A function that generates a random number[between 1 through 20]
def GRN():
  return random.randint(1, 20)

#Alice I
def Cal_A(g, x, n):
  A = g**x % n
  return A

#Alice II
def Cal_K1(B, x, n):
  K1 = B**x % n
  return K1

#Bob I
def Cal_B(g, y, n):
  B = g**y % n
  return B

#Bob II
def Cal_K2(A, y, n):
  K2 = A**y % n
  return K2

#--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--
#Key:
#1. Alice and Bob agree on a large prime number, n
#2. Alice and Bob agree on a generator g
#3. Alice and Bob make their own private key x and y [respectfully in that order]
#4. Alice and Bob calculate their public keys A and B [respectfully in that order] 
#5. Alice and Bob exchange their public keys A and B [respectfully in that order]
#6. Alice and Bob calculate their shared secret key, K1 and K2 [respectfully in that order]
#7. Key exchange successful
#--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--

def Master_C0De(who):
  One_n = GLP()
  Two_g = GRN()
  Three_x = GRN()
  Three_y = GRN()
  Four_A = Cal_A(Two_g, Three_x, One_n)
  Four_B = Cal_B(Two_g, Three_y, One_n)
  Six_K1 = Cal_K1(Four_B, Three_x, One_n)
  Six_K2 = Cal_K2(Four_A, Three_y, One_n)
  
  if who == "A":
    return Six_K1
  elif who == "B":
    return Six_K2
  else:
    return 784