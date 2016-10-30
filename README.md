# RS_private_key_calculator
A simple Python script that calculates RSA private keys given the primes p and q and the exponent e.

The script isn't meant to crack RSA encryption, it just  reconstructs the private key d, and it needs p and q to do that, meaning you still have to factor N to its primes p and q using ggnfs or QS(yafu). General number field sieve (gnfs) is the best known approach for large integers.

For more info refer to Google.
