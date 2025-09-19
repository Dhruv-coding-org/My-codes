import sys
sys.set_int_max_str_digits(1000000000)# Fibonacci sequence generator
sys.set_int_max_str_digits(1000000000)# Fibonacci sequence generator
z = int(input("Sequence ends at index:"))
a = 0
b = 1
print(a)  # Print first number (0)
print(b)  # Print second number (1)
for i in range(z- 2):  # z-2 because we already printed 2 numbers
    c = a + b
    print(c)
    a = b
    b = c
z = int(input("Sequece ends at index:"))
a = 0
b = 1
c = a+b
for i in range(z):
    print (c)
    a=b
    b=c
    c=(a+b)
    
print(c)   