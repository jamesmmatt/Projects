"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print
"FizzBuzz"
"""

def fizzBuz(lastNumber):
	numRange = range(1, (lastNumber + 1))

	for num in numRange:
		if (num%3 == 0 and (num%5 == 0)):
			num = "FizzBuzz"
		elif (num%3 == 0):
			num = "Fizz"
		elif (num%5 == 0):
			num = "Buzz"
		
		print(num)

print("Choose the last number: ")
fizzLastNumber = int(input())

fizzBuz(fizzLastNumber)

