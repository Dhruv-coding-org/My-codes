import numpy as np
a = np.array({'javvu','rohan','dhruv'})
f = np.array({'pok pok','kartik','harsh'})

z = [10,9,10,9,9,6,6,10,9,10]
x = [7,2,1,4,5,1,7,1,9,2]

g = sum(z)
b = sum(x)

print("Good people",a)
print (g, "This is the score of good people out of 100. ")

print("Bad people", f)
print(b,"This is the score of bad people out of 100. ")