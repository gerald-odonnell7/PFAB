Bradys = ["Mike", "Carol", "Marsha", "Jan", "Cindy", "Greg", "Peter", "Bobby", "Alice"]
numBradys = len(Bradys)
print numBradys
counter = 0
while counter < numBradys:
  print Bradys[counter]
  counter = counter + 1
#Sorted
Bradys.sort()
counter = 0
while counter < numBradys:
  print Bradys[counter]
  counter = counter + 1
#The For Loop below does not work--need some guidance with this
#For...In Loop
For x in range(0,8):
    print Bradys[x]
