"""
The Art of Computer Programming - Donald Knuth
Volume 1 Chapter 1 Section 1.1 Page 2

Euclid's Algorithm : Find the GCD of two numbers
Inputs : m,n
1. Divide m by n : remainder is r
2. If r = 0, GCD = n
3. Otherwise set m <-- n, n<-- r; Go to Step 1

Saroj Sahu 2019-02-27  V1.0
"""

print ('Type TWO non-zero integers')
num1 = num2 = 0

#   Make sure inputs are integers
while num1 == 0:
    num1 = input('first number ')
    try:
        num1 = int(num1)
    except:
        num1 = 0

while num2 == 0:
    num2 = input('second number ')
    try:
        num2 = int(num2)
    except:
        num2 = 0

#   Order them - Optional step
if num1 > num2:
    m = num1; n = num2
else:
    m = num2; n = num1

done = False
gcd = 'not found'

#    Main loop
while not done:
    r = m%n
    if r == 0:
        gcd = n
        break
    else:
        m = n
        n = r

print('GCD of '+str(num1)+' and '+str(num2)+' is '+ str(gcd) )
