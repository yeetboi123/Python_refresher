"""
Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data
https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3
"""

def main():
    
    num = 3 
    print(type(num))
    
    num_float = 3.14 
    print(type(num_float))
    
    print(3 ** 2 // 2)
    
    print(3 % 2)
    
    num = 1 
    num *= 10
    print(num)
    
    print(round(3.75,1)) # round to first digit after decimal 
    
    num1 = 3
    num2 = 2
    print(num1 != num2)
    
    num1 = '100'
    num2 = '200'
    
    num1 = int(num1) # casting string type to integer type 
    num2 = int(num2)
    
    print(num1 + num2)
    
if __name__ == '__main__':
    main()