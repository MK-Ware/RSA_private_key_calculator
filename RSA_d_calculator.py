#A simple python tool to calculate RSA private key (d) knowing the public exponent e, and the prime factors of the modulus N; p and q. By mc111
#import the required modules. Cryptomath is included with the tool, keep it in the same folder.
import os, sys

#This is Cryptomath Module, so we don't have to import the module everytime..
#I didn't make the module, you can find that module at:
#http://inventwithpython.com/hacking (BSD Licensed)

def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

#My work starts from here
#Disclaimer and some info
print ("################RSA private key reconstructor by MCoury...#####################")
print ("###############################################################################")
print ("               ##############################################                  ")
print ("                             DISCLAIMER                                     ")
print()
print (">>>This tool DOES NOT crack RSA encryption! It reconstructs the private ")
print ("   key from the public exponent e, and the primes p and q which you get by ")
print ("   factoring the modulus N...")
print()
print ("   for more info just google RSA...")
print()
print ("###############################################################################")
print()

#define the integers (you should replace these with the exponent e, and the primes p and q you acquired by factoring N using yafu or ggnfs)
e = int(input("Please provide the exponent e... "))
p = int(input("Please provide the prime p... "))
q = int(input("Please provide the prime q... "))
print()
print (">>>Calculating d and N...")
print()

#now the calculation (N is obviousely already known but I included it just to verify the factorization)
d = findModInverse(e, (p - 1) * (q - 1))
N = p * q

#tell the shell to print the numbers
print ("d =", d)
print()
print ("N =", N)
print()
print ("Success!")
print()

#Save the numbers to a text file

fo = open('results.txt', 'a')

print (">>>Writing the values to results.txt...")

print('_________________________________________________________________________________________', file = fo)
print ("##########Calculated by RSA(d) python tool.. By mcoury111.. Version 1.0.0##########", file = fo)
print ("", file = fo)
print ('''Prime factors are:

p = ''', p,'''
q = ''', q,'''

exponent e = ''',e, file = fo)
print(' ', file = fo)
print ("d =", (d), file = fo)
print ("N =", (N), file = fo)

fo.close()

print()
print ("Done!")

#now you can decrypt the RSA encrypted text using an appropriate program after giving it d. You can use the icluded rsaCipher.py tool on windows or linux. Kryptomat is a nice android app that can do a similar job. It's limited to 1023 bit or less keys.. but you ain't factoring anything greater than 512 anytime soon.. maybe a 768 bit key if you have access to the necessary resources.
