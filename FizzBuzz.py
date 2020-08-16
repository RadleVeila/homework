for x in range(100): # Задал количество символов
    if x % 3 == 0 and x % 5 == 0: # Задал условия для FizzBuzz(х делится по модулю на 3 и на 5)
        print('FizzBuzz') 
        continue # Для того, чтобы условие соблюдалось и дальше
    elif x % 3 == 0: # Задал условие для Fizz(х делится на 3)
        print('Fizz')
        continue
    elif x % 5 == 0: # Задал условие для Buzz(х делится на 5)
        print('Buzz')
        continue
    print(x)

