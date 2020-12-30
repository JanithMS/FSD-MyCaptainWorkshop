##getting the inputs from user
num1 = int(input('Enter the starting number: '))
num2 = int(input('Enter the ending number: '))

##function to find the number is prime number
def isPrime(num):
    for i in range (2, num):
        if(num % i == 0):
            return 0
    return 1
    
##finding the prime numbers in given range
prime_numbers = []
for j in range (num1, num2+1):
    if(isPrime(j) == 1):
        prime_numbers.append(j)

##printing the number in required format
mainString = 'Prime numbers between %d and %d are: ' % (num1, num2)
longString = ''
for k in prime_numbers:
    string = str(k)
    longString = longString+ string+ ' '
print(mainString+longString)
