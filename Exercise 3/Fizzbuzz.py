# The Problem
#
# "Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”."
#
# NOTE -> Must be in class and method format
class Fizzbuzz:
    def multiples():
        for number in range(1, 101):
            if number % 3 == 0 and number % 5 == 0:
                print('FizzBuzz')
                continue
            elif number % 3 == 0:
                print('Fizz')
                continue
            elif number % 5 == 0:
                print('Buzz')
                continue

            print(number)
Fizzbuzz.multiples()

