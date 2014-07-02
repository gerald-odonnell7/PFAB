import math

first = "Roger"

last = "Dorsey"

age = 46

print first, " ", last, " ", age

sideA = 12.55

sideB = 17.85

#x = (sideA * sideA) + (sideB * sideB)

#sideC = math.sqrt(x)
#print " ", sideC

operand1 = 95

operand2 = 64.5

a = operand1 + operand2

b = operand1 - operand2

c = operand1 * operand2

d = operand1 / operand2

e = operand1 % operand2

print operand1, " + ", operand2, " = ", a

print operand1, " - ", operand2, " = ", b

print operand1, " * ", operand2, " = ", c

print operand1, " / ", operand2, " = ", d

print operand1, " % ", operand2, " = ", e

#The code above is optimal because by not hard coding the operands into the output, it will require less work to modify the code if the amounts used for the operands change
