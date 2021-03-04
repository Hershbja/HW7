def FizzBuzz(test):
    for x in range (1, 101, 1):
        if (x % 5 == 0) and (x % 3 == 0) :
            if test == x:
                return "FizzBuzz"
            else:
                print("FizzBuzz")
        elif(x % 3 == 0):
            if test == x:
                return "Fizz"
            else:
                print("Fizz")
        elif(x% 5 == 0):
            if test == x:
                return "Buzz"
            else:
                print("Buzz")
        else:
            if test == x:
                return x
            else:
                print(x)
            
def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        