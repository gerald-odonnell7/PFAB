score1 = input("Enter the first test score")

score2 = input("Enter the second test score")

score3 = input("Enter the third test score")

score4 = input("Enter the fourth test score")

average = (score1 + score2 + score3 + score4)/4

print "The average test score is ", average

if average >= 90:
	print "Letter Grade: A"

  elif average >= 80:
	print "Letter Grade: B"

  elif average >= 70:
	print "Letter Grade: C"

  elif average >= 60:
	print "Letter Grade: D"

else:
	print "Letter Grade: F"
