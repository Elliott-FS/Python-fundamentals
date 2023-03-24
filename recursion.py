# Basic recursive function example
# Create a function that takes in an even number and prints 
# all even numbers before it. 

def EvenNums(num):
    print(num)
    if num == 2:
        return 2
    else: return EvenNums(num-2)

EvenNums(10)    
