"""n = int(input("Enter n:").strip())
is_prime = True #we assuming 
if n<=1: #if any user enter 0 or 1 
    is_prime = False # then it's not a prime
else:
    for i in range(2, n): #n or n-1 both can use 
        if n % i == 0: # n = 17 and i start from 2 so n=17 and i=2 until i = 16 no divisor found 
            is_prime = False # so this executes 
            break   # and braks the loop 
if is_prime: # proving 
    print(f"{n} is a Prime number ✅")
else:
    print(f"{n} is NOT a Prime number ❌")"""

