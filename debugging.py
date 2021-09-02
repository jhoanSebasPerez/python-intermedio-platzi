def divisors(num): 
    try: 
        assert num > 0, "Number should be grater than 0"
        divisors = [ i for i in range(1, num//2 + 1) if num % i == 0]
        divisors.append(num)
        return divisors 
    except ValueError as ve: 
        return ve

def run(): 
    try: 
        number = int(input("Type a number: "))
        print(divisors(number))
    except ValueError: 
        print("Please input a number value")

if __name__ == "__main__": 
    run()