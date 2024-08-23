from array import *

array1 =[1,2,3,4,5]
array2 = array1
array2[0] = 0
print(array1)

vals = array('i',[1,2,3,4,5,6,7])
print(vals)
length = len(vals)
print("the length is ",length)
sum_of_array = sum(vals)
print("sum of the array =", sum_of_array)


a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
