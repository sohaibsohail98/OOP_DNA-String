class Fizzbuzz: #Defining a class
    def multiples(): #Defining a function
        for number in range(1, 101): #Number ranging from 1 to 100, a FOR loop - look for remainders when finding multiples of 3 and 5
            if number % 3 == 0 and number % 5 == 0: #Multiples of 5 and 3
                print('FizzBuzz')
                continue
            elif number % 3 == 0: #Multiples of 3 only
                print('Fizz')
                continue
            elif number % 5 == 0: #Multiples of 5 only
                print('Buzz')
                continue

            print(number) #This prints out the numbers that aren't multiples of 3 or 5.
Fizzbuzz.multiples()
#This is calling the class and function.

