given_input = [int(a) for a in input().split()]
x = given_input[0]
y = given_input[1]
n = given_input[2]

for number in range(1, n+1):
    if(number % x == 0 and number % y == 0):
        print("FizzBuzz")
    elif(number % x == 0):
        print("Fizz")
    elif(number % y == 0):
        print("Buzz")
    else:
        print(number)
