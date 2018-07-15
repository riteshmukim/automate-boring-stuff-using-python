'''Write a function named collatz() that has one parameter named number. 
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.'''

def collatz(number):
    if number % 2 == 0 :
        return number // 2
    else:
        return 3 * number + 1

print('Enter number')
while True:
    try:
        num = int(input())
        val = collatz(num)
        print(val)
        if val == 1:
            break
    except ValueError:
        print('Please Enter a Number')
print('-'*50)

