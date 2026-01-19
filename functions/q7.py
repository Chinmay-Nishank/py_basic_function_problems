# SymPy (a Python library for symbolic mathematics)
# from sympy import isprime
# print(isprime(2))
def isprime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    print("number is a prime number : ",num)
print(isprime(5))    

