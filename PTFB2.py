""" 
Python Tutorial for Beginners 2: Strings - Working with Textual Data
Link: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2
"""

def main():
    
    message = "Hello world"
    print(message)
    
    # Use string formatting
    greeting = "Hello"
    name = "Robin"
    message = '{}, {}. Welcome!'.format(greeting, name)
    print(message)

    # Use f string
    message = f'{greeting} {name}. Welcome!'
    print(message)
    
    message = f'{greeting.upper()} {name}. Welcome!'
    print(message)
    
    print(dir(name))
    
if __name__ == '__main__':
    main()
    
