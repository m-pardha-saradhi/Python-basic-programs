
# square of first n
# natural numbers

# Method 1

def squaresum(n) :
	sm = 0
	for i in range(1, n+1) :
		sm = sm + (i * i)
	
	return sm

# Driven Program
n = int(input("Enter a number : "))
print(squaresum(n))

# This code is contributed by Nikita Tiwari.*/


# Method 2
# Proof
"""
We know,
(k + 1)3 = k3 + 3 * k2 + 3 * k + 1
We can write the above identity for k from 1 to n:
23 = 13 + 3 * 12 + 3 * 1 + 1 ......... (1)
33 = 23 + 3 * 22 + 3 * 2 + 1 ......... (2)
43 = 33 + 3 * 32 + 3 * 3 + 1 ......... (3)
53 = 43 + 3 * 42 + 3 * 4 + 1 ......... (4)
...
n3 = (n - 1)3 + 3 * (n - 1)2 + 3 * (n - 1) + 1 ......... (n - 1)
(n + 1)3 = n3 + 3 * n2 + 3 * n + 1 ......... (n)

Putting equation (n - 1) in equation n,
(n + 1)3 = (n - 1)3 + 3 * (n - 1)2 + 3 * (n - 1) + 1 + 3 * n2 + 3 * n + 1
         = (n - 1)3 + 3 * (n2 + (n - 1)2) + 3 * ( n + (n - 1) ) + 1 + 1

By putting all equation, we get
(n + 1)3 = 13 + 3 * Σ k2 + 3 * Σ k + Σ 1
n3 + 3 * n2 + 3 * n + 1 = 1 + 3 * Σ k2 + 3 * (n * (n + 1))/2 + n
n3 + 3 * n2 + 3 * n = 3 * Σ k2 + 3 * (n * (n + 1))/2 + n
n3 + 3 * n2 + 2 * n - 3 * (n * (n + 1))/2 = 3 * Σ k2
n * (n2 + 3 * n + 2) - 3 * (n * (n + 1))/2 = 3 * Σ k2
n * (n + 1) * (n + 2) - 3 * (n * (n + 1))/2 = 3 * Σ k2
n * (n + 1) * (n + 2 - 3/2) = 3 * Σ k2
n * (n + 1) * (2 * n + 1)/2  = 3 * Σ k2
n * (n + 1) * (2 * n + 1)/6  = Σ k2
(n * (n + 1) / 2) * (2 * n + 1) / 3 = Σ k2

"""
def squaresum(n) :
	return (n * (n + 1) / 2) * (2 * n + 1) / 3

# Driven Program
n = int(input("Enter a number : "))
print(squaresum(n))
