for x in range(100):
    
    fizz = x % 3 == 0
    buzz = x % 5 == 0
    
    if fizz and buzz:
        print('FizzBuzz')
    elif fizz:
        print('Fizz')
    elif buzz:
        print('Buzz')
    else:
        print(x)
    

